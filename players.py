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

    def __init__(self, rang, decor, fichier, x, y, couleurperso, angle = 0):
        pygame.sprite.Sprite.__init__(self)
        self.cote = "droite"
        self.rang = rang
        self.decor = decor
        self.fichier = fichier
        self.x = x
        self.y = y
        self.couleurperso = couleurperso
        self.image = pygame.image.load(self.fichier).convert_alpha()
        self.image_retourne = pygame.transform.flip(self.image, 1, 0)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.mask = pygame.mask.from_surface(self.image)
        self.parterre = False

        #vitesse du personnage (TEST)
        self.vitesse_x = 5
#        self.vitesse_y = 5
#        self.vitesse_saut = 5
        self.gravite = 0.01

        self.depart_timer, self.fin_timer = False, False
        self.sauter = 0

        self.font = pygame.font.Font(None, 20)

        self.angle = angle
        self.imgbaz = pygame.image.load("image/personnages/arme1.png").convert_alpha()
        self.imggren = pygame.image.load("image/personnages/arme2.png").convert_alpha()
        self.armeaffiche = self.imgbaz
        self.switch = 1

    def affiche(self, fenetre, vie, tour, numero):
        fenetre.blit(self.image, self.rect)
#afficher vie perso - TEST
        vie = str(vie)

        if self.couleurperso == "red":
            couleur = (255,0,0)
        if self.couleurperso == "blue":
            couleur = (0,0,255)
        vie = self.font.render(vie, 1, couleur)
        fenetre.blit(vie, (self.rect.x,self.rect.y-13))
        #afficher que l'arme du joueur
        if ((tour == 1 and self.couleurperso == "red") or (tour == 2 and self.couleurperso == "blue")) and (self.rang == numero):
            self.armeaffiche = rotation(self.armeaffiche, self.angle)
            fenetre.blit(self.armeaffiche, (self.rect.x+10,self.rect.y+10))

#afficher pos perso - TEST
#        char_x = str(self.rect.x)
#        char_y = str(self.rect.y)
#        font = pygame.font.Font(None, 50)
#        xx = font.render(char_x, 1, (0,0,0))
#        fenetre.blit(xx, (10,10))
#        yy = font.render(char_y, 1, (0,0,0))
#        fenetre.blit(yy, (10,50))

    def mouvement(self, tour, numero, saut, gauche, droite, debug, angle, switch):
# test debug------------
        if debug == True:
            self.rect.x = self.x
            self.rect.y = self.y
#-----------------------

        vitesse_y = 5
        vitesse_saut = 5

        #déterminer si c'est son tour de jeu :
        if ((tour == 1 and self.couleurperso == "red") or (tour == 2 and self.couleurperso == "blue")) and (self.rang == numero):
            #inclinaison arme
            if angle == "+":
                self.angle += 1

            if angle == "-":
                self.angle -= 1
            print(self.angle)

            #afficher arme
            if switch != self.switch:
                self.switch = switch
            if self.switch == 1:
                self.armeaffiche = self.imgbaz
            if self.switch == 2:
                self.armeaffiche = self.imggren

            if droite == True:
                self.rect.x += self.vitesse_x
                if self.cote == "gauche":
                    self.cote = "droite"
                    self.image = pygame.image.load(self.fichier).convert_alpha()
                    self.mask = pygame.mask.from_surface(self.image)
                    self.armeaffiche =  pygame.transform.flip(self.armeaffiche, 1, 0)

            if gauche == True:
                self.rect.x -= self.vitesse_x
                if self.cote == "droite":
                    self.cote = "gauche"
                    self.image = self.image_retourne
                    self.mask = pygame.mask.from_surface(self.image)
                    self.armeaffiche =  pygame.transform.flip(self.armeaffiche, 1, 0)

            if saut and self.parterre:
                self.depart_timer = True
                self.fin_timer = False
                self.rect.y -= vitesse_saut
        else:
            saut = 0
            droite = 0
            gauche = 0

        if not saut:
            self.fin_timer = True

        if self.depart_timer == True:
            self.sauter = pygame.time.get_ticks() + 400
            self.depart_timer = False
        if pygame.time.get_ticks() > self.sauter:
            self.fin_timer = True

        if not self.parterre:
            if self.fin_timer:
                vitesse_y += self.gravite  #appliquer la gravite
			 #attraction maximale
                if vitesse_y > 30:
                    vitesse_y = 30
                self.rect.y += vitesse_y
            if not self.fin_timer:
                self.rect.y -= vitesse_saut #sauter

		# faire la collision avec les x
        self.collision(self.vitesse_x, 0, gauche, droite, False)
        if saut == False:
            self.rect.y += vitesse_y
		#en l'air
        self.parterre = False
		# faire la collision avec les y
        self.collision(0, vitesse_y, False, False, saut)

    def collision(self, vitesse_x, vitesse_y, gauche, droite, saut):
        while (pygame.sprite.collide_mask(self, self.decor)):
            #empeche le perso d'etre blitte dans la map
            if gauche == True: self.rect.x += vitesse_x
            if droite == True: self.rect.x -= vitesse_x
            if saut == False:
                #pour que le perso reste sur le sol
                while (pygame.sprite.collide_mask(self, self.decor)):
                    self.rect.y -= 1
                self.parterre = True
                vitesse_y = 0

# ----------------------BUG----------------------------- #
            if saut == True:
#                while (pygame.sprite.collide_mask(self, self.decor)):
                self.rect.y += self.vitesse_saut
                self.parterre = False
                vitesse_y = 0

 #           if saut == True:
 #               #pour que le perso reste sur le sol
 #               self.rect.y += self.vitesse_y
 #               self.parterre = True
 #               self.vitesse_y = 0



        #    and (pygame.sprite.collide_mask(self, self.decor)):
#                    self.rect.y += vitesse_y
#                vitesse_y = 0
         #       self.rect.y += vitesse_y
         #       self.vitesse_y = 0
         #       self.fin_timer = True

def rotation(image, angle): #rotation arme
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image