#-------------------------------------------------------------------------------
# Name:        constantes
#
# Author:      sl-prog et regisseur
#
# Licence:     <GNU GENERAL PUBLIC LICENSE>
#-------------------------------------------------------------------------------

import pygame
from pygame.locals import *

#Dimension ecran
largeur_ecran = 800
hauteur_ecran = 560

#Titre ecran
titre_fenetre = 'Mountain Domination'
fenetre = pygame.display.set_mode((largeur_ecran, hauteur_ecran)) #fenetre de 640*480

#Images
icon = "image/icon.png"
background = "image/ciel.png"
mountain = "image/map-tunnel.png"
escargot_rouge = "image/esc-red.png"
escargot_bleu = "image/esc-blue.png"

bazooka ="image/bazooka" #image arme
grenade = "image/prj_grenade.png"  #image projectile aussi utilisee pour image arme
rocket = "image/prj_rocket.png" #image projectile

arme1 = pygame.image.load("image/bazooka.png").convert_alpha()
arme2 = pygame.image.load("image/grenade.png").convert_alpha()
chargement0 = pygame.image.load("image/barre0.png").convert_alpha()
chargement1 = pygame.image.load("image/barre1.png").convert_alpha()
chargement2 = pygame.image.load("image/barre2.png").convert_alpha()
chargement3 = pygame.image.load("image/barre3.png").convert_alpha()
chargement4 = pygame.image.load("image/barre4.png").convert_alpha()
horloge = pygame.image.load("image/horloge.png").convert_alpha()


#vitesse et positions des personnages (TEST)
vitesse_perso_x = 5
vitesse_perso_y = 5
viemax = 100

gauche = False
droite = False
saut = False
gravite = 0.01
vitesse_saut= 5

duree_tour = 2
seconde = pygame.time.get_ticks() + 1000
tempsjeu = duree_tour

numero = 0 #doit rester a  0

debug = False

#TEST
sens_perso = True

#variable fin de la boucle principale
done=False
