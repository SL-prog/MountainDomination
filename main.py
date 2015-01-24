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

#Chargement et collage des personnages - test
image = pygame.image.load(escargot_rouge).convert_alpha()
image_retourne = pygame.transform.flip(image, 1, 0)
rouge = players.Player(image,image_retourne,200,300)
# perso_bleu = pygame.image.load(escargot_bleu).convert_alpha()
# fenetre.blit(perso_bleu, (100,300))

#Rafraichissement/mise a  jour de l'ecran
pygame.display.flip()

#Simule des appuis très rapide sur la touche quand on la maintient
pygame.key.set_repeat(1, 10)

#BOUCLE Principale
while not done:

#Quitter le jeu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
#Front montant appuis touche
        elif event.type == pygame.KEYDOWN:
#déplacement droite-gauche
            if event.key == pygame.K_LEFT:
                sens_perso= False
                rouge.gauche(vitesse_perso)
            elif event.key == pygame.K_RIGHT:
                sens_perso= True
                rouge.droite(vitesse_perso)
#orientation arme - TEST : changement vitesse
#           if event.key == pygame.K_UP:
#                rouge.augmente(1)
#            if event.key == pygame.K_DOWN:
#                rouge.augmente(-1)
#Front descendant appuis touche
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                rouge.gauche(0)
            elif event.key == pygame.K_RIGHT:
                rouge.droite(0)

#Afficher le fond du jeu
    fenetre.blit(fond, (0,0))

#Afficher sens - TEST
    if sens_perso==True:
        charsens = 'droite'
    else:
        charsens = 'gauche'
    font = pygame.font.Font(None, 50)
    textsens = font.render(charsens, 1, (0,0,0))
    fenetre.blit(textsens, (280,10))

#Afficher les personnages - TEST
    rouge.affiche(fenetre,sens_perso)

#Rafraichissement/mise a  jour de l'ecran
    pygame.display.flip()

#Limitation de vitesse de la boucle
    pygame.time.Clock().tick(30)

pygame.quit()