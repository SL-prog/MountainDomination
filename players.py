#-------------------------------------------------------------------------------
# Name:        Players
#
# Author:      sl-prog
#
# Licence:     <GNU GENERAL PUBLIC LICENSE>
#-------------------------------------------------------------------------------

import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):

    def __init__(self, decor, fichier, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.decor = decor
        self.fichier = fichier
        self.x = x
        self.y = y
        self.image = pygame.image.load(self.fichier).convert_alpha()
        self.image_retourne = pygame.transform.flip(self.image, 1, 0)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.mask = pygame.mask.from_surface(self.image)
        self.parterre = False

    def affiche(self, fenetre):
        fenetre.blit(self.image, self.rect)

#afficher pos perso - TEST
        char_x = str(self.rect.x)
        char_y = str(self.rect.y)
        font = pygame.font.Font(None, 50)
        xx = font.render(char_x, 1, (0,0,0))
        fenetre.blit(xx, (10,10))
        yy = font.render(char_y, 1, (0,0,0))
        fenetre.blit(yy, (10,50))

    def mouvement(self, vitesse_x, vitesse_y, gravite, saut, gauche, droite):
        if droite == True:
            self.rect.x += vitesse_x
            self.image = pygame.image.load(self.fichier).convert_alpha()

        if gauche == True:
            self.rect.x -= vitesse_x
            self.image = self.image_retourne

        if saut == True:
            if self.parterre == True:
                self.rect.y -= vitesse_y
        if not self.parterre:
            vitesse_y += gravite  #appliquer la gravite
			#attraction maximale
            if vitesse_y > 30:
                vitesse_y = 30
		# faire la collision avec les x
        self.collision(vitesse_x, 0)
        self.rect.y += vitesse_y
		#en l'air
        self.parterre = False;
		# faire la collision avec les y
        self.collision(0, vitesse_y)

    def collision(self, vitesse_x, vitesse_y):
        while (pygame.sprite.collide_mask(self, self.decor)):
            if vitesse_x > 0: self.rect.x -= vitesse_x
            if vitesse_x < 0: self.rect.x += vitesse_x
            if vitesse_y > 0:
                self.rect.y -= vitesse_y
                self.parterre = True
                vitesse_y = 0
            if vitesse_y < 0:
                self.rect.y += vitesse_y