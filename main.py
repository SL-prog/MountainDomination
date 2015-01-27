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
from pygame import font, mask, Surface, SRCALPHA
from pygame.sprite import Sprite, collide_mask, collide_rect
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

#Chargement de la montagne + mask + rect
decor = pygame.image.load(mountain).convert_alpha()
decor_mask = pygame.mask.from_surface(decor)
decor_rect = decor.get_rect()

#Chargement et collage des personnages - test - + mask
image = pygame.image.load(escargot_rouge).convert_alpha()
image_mask = pygame.mask.from_surface(image)
image_rect = image.get_rect()
image_retourne = pygame.transform.flip(image, 1, 0)

rouge = players.Player(image,image_retourne,x_rouge,y_rouge)
# perso_bleu = pygame.image.load(escargot_bleu).convert_alpha()
# fenetre.blit(perso_bleu, (100,300))

#Rafraichissement/mise aÂ  jour de l'ecran
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
                sens_perso = False
                gauche = True
            elif event.key == pygame.K_RIGHT:
                sens_perso = True
                droite = True
#saut
            if event.key == pygame.K_SPACE:
                saut=True


#Front descendant appuis touche
        elif event.type == pygame.KEYUP:
#fin deplacement droite-gauche
            if event.key == pygame.K_LEFT:
                gauche = False
            elif event.key == pygame.K_RIGHT:
                droite = False
#fin saut
            if event.key == pygame.K_SPACE:
                saut=False

#Afficher le fond du jeu
    fenetre.blit(fond, (0,0))

#Afficher la montagne
    fenetre.blit(decor, (-80,0))

#GÃ©rer mouvement personnages
    rouge.mouvement(vitesse_perso_x, vitesse_perso_y, gravite, saut, gauche, droite, image_rect, decor_rect)

#Afficher les personnages - TEST
    rouge.affiche(fenetre,sens_perso)

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