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

    def __init__(self, decor, perso, perso_retourne, image, image_retourne, x, y):
        self.x = x
        self.y = y
        self.image=image
        self.image_retourne=image_retourne
        self.perso = perso
        self.perso_retourne = perso_retourne
        self.decor = decor
        self.parterre = False


    def affiche(self, fenetre, sens_perso, image_rect):
        if sens_perso==True:
            fenetre.blit(self.image, image_rect)
        if sens_perso==False:
            fenetre.blit(self.image_retourne, image_rect)

    def mouvement(self, vitesse_x, vitesse_y, gravite, saut, gauche, droite):
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
        self.collision(vitesse_x, 0)
        self.y += vitesse_y
		#en l'air
        self.parterre = False;
		# faire la collision avec les y
        self.collision(0, vitesse_y)

    def collision(self, vitesse_x, vitesse_y):
        while (pygame.sprite.collide_mask(self.perso, self.decor)) or (pygame.sprite.collide_mask(self.perso_retourne, self.decor)) :
            if vitesse_x > 0: self.x -= vitesse_x
            if vitesse_x < 0: self.x += vitesse_x
            if vitesse_y > 0:
                self.y -= vitesse_y
                self.parterre = True
                vitesse_y = 0
            if vitesse_y < 0:
                self.y += vitesse_y
