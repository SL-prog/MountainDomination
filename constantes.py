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

#son
sonmenu = pygame.mixer.Sound("sons/menu.wav")
sonjeu = pygame.mixer.Sound("sons/jeu.wav")
sonexplosion = pygame.mixer.Sound("sons/explosion.wav")
songagner = pygame.mixer.Sound("sons/gagner.wav")

#Titre ecran
titre_fenetre = 'Mountain Domination'
fenetre = pygame.display.set_mode((largeur_ecran, hauteur_ecran)) #fenetre de 640*480
icon = "image/interface/icon.png"
pygame.display.set_icon(pygame.image.load(icon))

#bazooka ="image/bazooka" #image arme
grenade = "image/personnages/prj_grenade.png"  #image projectile aussi utilisee pour image arme
rocket = "image/personnages/prj_rocket.png" #image projectile

arme1 = pygame.image.load("image/interface/bazooka.png").convert_alpha()
arme2 = pygame.image.load("image/interface/grenade.png").convert_alpha()
chargement0 = pygame.image.load("image/interface/barre0.png").convert_alpha()
chargement1 = pygame.image.load("image/interface/barre1.png").convert_alpha()
chargement2 = pygame.image.load("image/interface/barre2.png").convert_alpha()
chargement3 = pygame.image.load("image/interface/barre3.png").convert_alpha()
chargement4 = pygame.image.load("image/interface/barre4.png").convert_alpha()
horloge = pygame.image.load("image/interface/horloge.png").convert_alpha()

tourjoueur1 = pygame.image.load("image/interface/tourjoueur1.png").convert_alpha()
tourjoueur2 = pygame.image.load("image/interface/tourjoueur2.png").convert_alpha()
congratulations = pygame.image.load("image/interface/congratulations.png")

#initialiser les touches de commande
gauche = False
droite = False
saut = False
angle = ""

tombe1 =  "image/personnages/tombe1.png"
tombe2 =  "image/personnages/tombe2.png"

expl1 = pygame.image.load("image/armes/expl1.png").convert_alpha()
expl2 = pygame.image.load("image/armes/expl2.png").convert_alpha()

tempsattente = 1000
seconde = pygame.time.get_ticks() + tempsattente

numerorouge = 0 #doit rester a 0
numerobleu = 0

#TEST
sens_perso = True
debug = False