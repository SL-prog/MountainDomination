#-------------------------------------------------------------------------------
# Name:        Epic Mountain Battle
#
# Author:      sl-prog
#
# Licence:     <GNU GENERAL PUBLIC LICENSE>
#-------------------------------------------------------------------------------

#Importation et initialisation de la bibliotheque Pygame
import pygame
from pygame.locals import *
pygame.init()

#Importation des autres programmes
from constantes import *
import menu
import mapgest
import players
import interface

#Ouverture de la fenetre Pygame
fenetre = pygame.display.set_mode((largeur_ecran, hauteur_ecran), RESIZABLE) #fenetre de 640*480
pygame.display.set_caption(titre_fenetre)
pygame.display.set_icon(pygame.image.load(icon))

#Chargement du fond
fond = pygame.image.load(background).convert()

#Chargement de la montagne + mask + rect -> creer class
decor = pygame.sprite.Sprite()
decor.image = pygame.image.load(mountain).convert_alpha()
decor.rect = decor.image.get_rect()
decor.rect.topleft = 0, 0
decor.mask = pygame.mask.from_surface(decor.image)

rouge = players.Player(decor, escargot_rouge, x_rouge, y_rouge)
#bleu = players.Player(decor, escargot_bleu, x_bleu, y_bleu)

#Rafraichissement/mise a jour de l'ecran
pygame.display.flip()

#Simule des appuis tres rapide sur la touche quand on la maintient
pygame.key.set_repeat(1, 1) #(dure appui, temps entre chaque appui)

#BOUCLE Principale
while not done:
#Quitter le jeu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
#Front montant appuis touche
        elif event.type == pygame.KEYDOWN:
#deplacement droite-gauche
            if event.key == pygame.K_LEFT:
                sens_perso = False #TEST
                gauche = True
            elif event.key == pygame.K_RIGHT:
                sens_perso = True #TEST
                droite = True
#saut
            if event.key == pygame.K_UP:
                saut=True


#Front descendant appuis touche
        elif event.type == pygame.KEYUP:
#fin deplacement droite-gauche
            if event.key == pygame.K_LEFT:
                gauche = False
            elif event.key == pygame.K_RIGHT:
                droite = False
#fin saut
            if event.key == pygame.K_UP:
                saut=False

#Gerer mouvement personnages
    rouge.mouvement(vitesse_perso_x, vitesse_perso_y, gravite, saut, gauche, droite)
#    bleu.mouvement(vitesse_perso_x, vitesse_perso_y, gravite, saut, gauche, droite)

#Afficher le fond du jeu
    fenetre.blit(fond, (0,0))

#Afficher la montagne -- Creer class
    fenetre.blit(decor.image, decor.rect)

#Afficher les personnages - TEST
    rouge.affiche(fenetre)
#    bleu.affiche(fenetre)

#Afficher sens - TEST
    if sens_perso==True:
        charsens = 'droite'
        couleursens=(0,255,0)
    else:
        charsens = 'gauche'
        couleursens = (255,0,0)
    font = pygame.font.Font(None, 50)
    textsens = font.render(charsens, 1, couleursens)
    fenetre.blit(textsens, (260,10))

#Rafraichissement/mise a jour de l'ecran
    pygame.display.flip()

#Limitation de vitesse de la boucle
    pygame.time.Clock().tick(30)

pygame.quit()