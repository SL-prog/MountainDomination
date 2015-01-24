#-------------------------------------------------------------------------------
# Name:        Players
#
# Author:      sl-prog
#
# Licence:     <GNU GENERAL PUBLIC LICENSE>
#-------------------------------------------------------------------------------

import pygame
from pygame.locals import *

class Player:

    def __init__(self, image, image_retourne, x=0, y=0, vitesse=0):
        self.x = x
        self.y = y
        self.image=image
        self.image_retourne=image_retourne
        self.vitesse = vitesse
    def affiche(self, fenetre, sens_perso):
        if sens_perso==True:
            fenetre.blit(self.image, (self.x,self.y))
        if sens_perso==False:
            fenetre.blit(self.image_retourne, (self.x,self.y))
    def droite(self,valeur_vitesse):
        self.vitesse=valeur_vitesse
        self.x += self.vitesse
    def gauche(self,valeur_vitesse):
        self.vitesse=valeur_vitesse
        self.x -= self.vitesse
