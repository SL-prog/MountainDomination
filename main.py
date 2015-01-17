#-------------------------------------------------------------------------------
# Name:        Epic Mountain Battle
#
# Author:      sl-prog
#
# Licence:     <GNU GENERAL PUBLIC LICENSE>
#-------------------------------------------------------------------------------

#Importation et initialisation de la bibliothèque Pygame
import pygame
from pygame.locals import *
pygame.init()

#Importation des autres programmes
import menu
import mapgest
import players
import interface

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480), RESIZABLE) #fenêtre de 640*480 modifiable
pygame.display.set_caption('Mountain Domination')
pygame.display.set_icon(pygame.image.load("image/icon.png"))

#Chargement et collage du fond
fond = pygame.image.load("image/background.png").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage des personnages - test
perso_rouge = pygame.image.load("image/esc-red.png").convert_alpha()
fenetre.blit(perso_rouge, (200,300))

perso_bleu = pygame.image.load("image/esc-blue.png").convert_alpha()
fenetre.blit(perso_bleu, (100,300))

#Rafraîchissement/mise à jour de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = 1
while continuer:
	continuer = int(input())   #entrer 0 pour quitter
pygame.quit()