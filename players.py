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

    def __init__(self, rang, decor, projectile, fichier, x, y, vie, couleurperso, tombe):
        pygame.sprite.Sprite.__init__(self)
        self.cote = "droite"
        self.rang = rang
        self.x = x
        self.y = y
        self.vie = vie
        self.vivant = True

        self.decor = decor
        self.couleurperso = couleurperso
        self.tombe = pygame.image.load(tombe).convert_alpha()
        self.fichier = fichier
        self.image = pygame.image.load(self.fichier).convert_alpha()
        self.image_retourne = pygame.transform.flip(self.image, 1, 0)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.mask = pygame.mask.from_surface(self.image)

        self.parterre = False

        #vitesse du personnage
        self.vitesse_x = 5
        self.vitesse_y = 5
        self.vitesse_saut = 5
        self.gravite = 0.01
        self.depart_timer, self.fin_timer = False, False
        self.sauter = 0 #duree initiale saut

        self.angle = 0
        self.imgbaz = pygame.image.load("image/armes/arme1.png").convert_alpha()
        self.imggren = pygame.image.load("image/armes/arme2.png").convert_alpha()
        self.armeaffiche = self.imgbaz
        self.switch = 1

        self.prjbaz = pygame.image.load("image/armes/prj1.png").convert_alpha()
        self.prjgren = pygame.image.load("image/armes/prj2.png").convert_alpha()

        self.afficherprj = False

        self.font = pygame.font.Font(None, 20)

        self.projectile = projectile

    def affiche(self, fenetre, tour, numero):
        if self.vivant:
            fenetre.blit(self.image, self.rect)
            #afficher vie perso
            vie = str(self.vie)

            if self.couleurperso == "red":
                couleur = (255,0,0)
            if self.couleurperso == "blue":
                couleur = (0,0,255)
            vie = self.font.render(vie, 1, couleur)
            fenetre.blit(vie, (self.rect.x,self.rect.y-13))
            #afficher uniquement l'arme du joueur actuel
            if ((tour == 1 and self.couleurperso == "red") or (tour == 2 and self.couleurperso == "blue")) and (self.rang == numero):
                self.armeaffiche = rotation(self.armeaffiche, self.angle)
                if self.cote =="droite":
                    fenetre.blit(self.armeaffiche, (self.rect.x+14,self.rect.y+6))
                if self.cote =="gauche":
                    fenetre.blit(self.armeaffiche, (self.rect.x-10,self.rect.y+6))

        if not(self.vivant):
            if (self.rect.x>=0) and (self.rect.x<=800) and (self.rect.y>=0) and (self.rect.y<=480):
                fenetre.blit(self.tombe, self.rect)

        if self.afficherprj == True:
            fenetre.blit(self.projectile.image, (20,20))

#afficher pos perso - TEST --------------------------
        if ((tour == 1 and self.couleurperso == "red") or (tour == 2 and self.couleurperso == "blue")) and (self.rang == numero):
            char_x = str(self.rect.x)
            char_y = str(self.rect.y)
            font = pygame.font.Font(None, 50)
            xx = font.render(char_x, 1, (0,0,0))
            fenetre.blit(xx, (10,10))
            yy = font.render(char_y, 1, (0,0,0))
            fenetre.blit(yy, (10,50))
#--------------------------

    def mouvement(self, tour, numero, saut, gauche, droite, debug, angle, switch):
# test debug------------
        if debug == True:
            self.rect.x = self.x
            self.rect.y = self.y
#-----------------------
        if self.rang == 1 and self.couleurperso == "red":
            self.vie = self.vie -1
        #determiner si c'est son tour de jeu :
        if ((tour == 1 and self.couleurperso == "red") or (tour == 2 and self.couleurperso == "blue")) and (self.rang == numero) and self.afficherprj == False:
            #inclinaison arme
            if angle == "+":
                if self.cote == "droite" and self.angle<90:
                    self.angle += 5
                if self.cote == "gauche" and self.angle>-90:
                    self.angle -= 5

            if angle == "-":
                if self.cote == "droite" and self.angle>-90:
                    self.angle -= 5
                if self.cote == "gauche" and self.angle<90:
                    self.angle += 5

            #afficher arme
            if switch != self.switch:
                self.switch = switch
            if self.switch == 1:
                self.armeaffiche = self.imgbaz
                self.projectile.image = self.prjbaz
            if self.switch == 2:
                self.armeaffiche = self.imggren
                self.projectile.image = self.prjgren

            if droite == True:
                self.rect.x += self.vitesse_x
                if self.cote == "gauche":
                    self.cote = "droite"
                    self.image = pygame.image.load(self.fichier).convert_alpha()
                    self.mask = pygame.mask.from_surface(self.image)
                    self.imgbaz =  pygame.transform.flip(self.imgbaz, 1, 0)
                    self.imggren =  pygame.transform.flip(self.imggren, 1, 0)
                    self.angle = -self.angle

            if gauche == True:
                self.rect.x -= self.vitesse_x
                if self.cote == "droite":
                    self.cote = "gauche"
                    self.image = self.image_retourne
                    self.mask = pygame.mask.from_surface(self.image)
                    self.imgbaz =  pygame.transform.flip(self.imgbaz, 1, 0)
                    self.imggren =  pygame.transform.flip(self.imggren, 1, 0)
                    self.angle = -self.angle

            if saut and self.parterre:
                self.depart_timer = True
                self.fin_timer = False
                self.rect.y -= self.vitesse_saut #début saut

        else: #si ce n'est pas son tour
            saut = 0
            droite = 0
            gauche = 0

        if not(saut):
            self.fin_timer = True

        if self.depart_timer == True:
            self.sauter = pygame.time.get_ticks() + 400 #duree saut 400ms
            self.depart_timer = False
        if pygame.time.get_ticks() > self.sauter:
            self.fin_timer = True

        if not(self.parterre):
            if self.fin_timer:
                self.vitesse_y += self.gravite  #appliquer la gravite
			     #limiter attraction maximale
                if self.vitesse_y > 10:
                    self.vitesse_y = 10
                self.rect.y += self.vitesse_y
            if not(self.fin_timer):
                self.rect.y -= self.vitesse_saut #sauter

        #reinitialiser vitesse y
        if self.parterre:
            self.vitesse_y = 5

		# faire la collision avec les x
        self.collision(gauche, droite, False)
        if saut == False:
            self.rect.y += self.vitesse_y
		#en l'air
        self.parterre = False
		# faire la collision avec les y
        self.collision(False, False, saut)

        #si plus de points de vie, devenir une tombe, et etre mort
        if self.vie <= 0:
            self.mask = pygame.mask.from_surface(self.tombe)
            self.vie = 0
            self.vivant = False

    def collision(self, gauche, droite, saut):
        if (pygame.sprite.collide_mask(self, self.decor)):
            if gauche == True: self.rect.x += self.vitesse_x
            if droite == True: self.rect.x -= self.vitesse_x

            if saut == False and self.fin_timer == True:
                #pour que le perso reste sur le sol
                while (pygame.sprite.collide_mask(self, self.decor)):
                    self.rect.y -= 1
                self.parterre = True
            if saut == True and not(self.parterre):
                #pour que le perso reste sur le sol
                while (pygame.sprite.collide_mask(self, self.decor)):
                    self.rect.y += 1
                self.fin_timer = True


    def tir(self, chargement, tour, numero):
        if ((tour == 1 and self.couleurperso == "red") or (tour == 2 and self.couleurperso == "blue")) and (self.rang == numero):
            self.afficherprj = True


def rotation(image, angle): #rotation arme, par le milieu de l'image
    origine_rectangle = image.get_rect()
    rotation_image = pygame.transform.rotate(image, angle)
    rotation_rectangle = origine_rectangle.copy()
    rotation_rectangle.center = rotation_image.get_rect().center
    rotation_image = rotation_image.subsurface(rotation_rectangle).copy()
    return rotation_image