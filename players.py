#-------------------------------------------------------------------------------
# Name:        Players
#
# Author:      sl-prog
#
# Licence:     <GNU GENERAL PUBLIC LICENSE>
#-------------------------------------------------------------------------------

import pygame
from pygame.locals import *
from pygame import font, mask, Surface, SRCALPHA
from pygame.sprite import Sprite, collide_mask, collide_rect

class Player:

    def __init__(self, image, image_retourne, x=0, y=0):
        self.x = x
        self.y = y
        self.image=image
        self.image_retourne=image_retourne
        self.parterre = False

    def affiche(self, fenetre, sens_perso):
        if sens_perso==True:
            fenetre.blit(self.image, (self.x,self.y))
        if sens_perso==False:
            x=x
            #fenetre.blit(self.image_retourne, (self.x,self.y))

    def mouvement(self, vitesse_x, vitesse_y, gravite, saut, gauche, droite, perso, carte):
        if droite == True:
            self.x += vitesse_x
        if gauche == True:
            self.x -= vitesse_x
        if saut == True:
            if self.parterre == True:
                self.y -= vitesse_y
        if not self.parterre:
            vitesse_y += gravite  #appliquer la gravite
			#attraction maximale
            if vitesse_y > 30:
                vitesse_y = 30
		# faire la collision avec les x
        self.collision(vitesse_x, 0, perso, carte)
        self.y += vitesse_y
		#en l'air
        self.parterre = False;
		# faire la collision avec les y
        self.collision(0, vitesse_y, perso, carte)

    def collision(self, vitesse_x, vitesse_y, perso, carte):
        while pygame.sprite.collide_mask(perso, carte):
            if vitesse_x > 0: self.x -= vitesse_x
            if vitesse_x < 0: self.x += vitesse_x
            if vitesse_y > 0:
                    self.y -= vitesse_y
                    self.parterre = True
                    vitesse_y = 0
            if vitesse_y < 0: self.y += vitesse_y
