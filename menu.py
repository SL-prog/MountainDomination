#-------------------------------------------------------------------------------
# Name:        Menu
#
# Author:      Bretton's power
#
# Licence:     <GNU GENERAL PUBLIC LICENSE>
#-------------------------------------------------------------------------------

import pygame
from pygame.locals import *
from constantes import *

def menuprincipal():
    # Initialisation de la fenetre d'affichage
    pygame.display.set_caption("Mountain Domination - Menu")

    couleur_quitter = (30,127,203)
    couleur_jouer = (167,103,38)
   #Police des boutons textes
    font = pygame.font.Font("police.ttf", 26)
    # Remplissage de l'arriere-plan
    fond = pygame.image.load("image/backgrounds/backgroundmenu.png").convert()
    # Boucle d'evenements
    while 1:
        fenetre.blit(fond, (0,0))
      #Changement des couleurs des boutons du menu, si la souris se met dessus.
        for event in pygame.event.get():

            if event.type == QUIT:
                return 0

            if event.type == MOUSEMOTION:
                if (event.pos[0] >= 312)  and (event.pos[0]<= 486) and (event.pos[1] >= 359)  and (event.pos[1] <= 408) :
                    couleur_quitter = (127,35,128)

                elif (event.pos[0] >= 312)  and (event.pos[0]<= 486) and (event.pos[1] >= 249)  and (event.pos[1] <= 298) :
                    couleur_jouer = (127,35,128)
                else:
                    couleur_quitter = (30,127,203)
                    couleur_jouer = (167,103,38)


        #Sortie du jeu, si il y a clic sur le bouton "jouer"

            if event.type == MOUSEBUTTONDOWN and event.button == 1 and (event.pos[0] >= 312)  and (event.pos[0]<= 486) and (event.pos[1] >= 249)  and (event.pos[1] <= 298):
                return 2

        #Passage au "second menu", si il y'a clic sur le bouton "quitter"

            if event.type == MOUSEBUTTONDOWN and event.button == 1 and (event.pos[0] >= 312)  and (event.pos[0]<= 486) and (event.pos[1] >= 359)  and (event.pos[1] <= 408):
                return 0
    # Affichage du bouton Jouer et son texte
    # Voici le bouton, et son cadre:
        pygame.draw.rect(fenetre,couleur_jouer, (309, 246, 180, 55), 0) # avec : x,y, longueur, Epaisseur
        pygame.draw.rect(fenetre,(255,255,255), (309, 246, 180, 55), 2)
        text = font.render("JOUER", 1, (255, 255, 255))
    # Et voici le texte :
        fenetre.blit(text, (354,257))

    # Affichage du bouton QUITTER et son texte
    # Voici le bouton, et son cadre :
        pygame.draw.rect(fenetre,couleur_quitter, (309, 356, 180, 55), 0) # avec : x,y, longueur, Epaisseur
        pygame.draw.rect(fenetre,(255,255,255), (309, 356, 180, 55), 2)
        text = font.render("QUITTER", 1, (255, 255, 255))
    # Et voici le texte :
        fenetre.blit(text, (333,368))

        pygame.display.flip()



#---------------------------------------------------------------------------------------
#Nouvelle fonction
#---------------------------------------------------------------------------------------

def menumap():
    #initialisation variables
    couleur_rect1 = (198,8,0)
    couleur_rect2 = 0
    couleur_rect3 = 0
    couleur_rect4 = 0
    couleur_rect5 = 0
    couleur_rect6 = 0
    couleur_retour = (30,127,203)
    couleur_suivant = (167,103,38)
    select = 0
    fondchoix = "image/backgrounds/backmap-dune.png"
    mapchoix = "image/maps/map-dune.png"
    # Initialisation de la fenetre d'affichage
    pygame.display.set_caption("Mountain Domination - Choix map")

    # Remplissage de l'arriere-plan
    fond = pygame.image.load("image/backgrounds/backgroundmenumap.png").convert()
   #Police des boutons textes
    font = pygame.font.Font("police.ttf", 26)

    # Boucle infinie
    while 1:
        # Blitter le tout dans la fenetre
        fenetre.blit(fond, (0, 0))
    #Boutons retour (1) et suivant (2)

     # 1) Voici le bouton retour, et son cadre :
        pygame.draw.rect(fenetre,couleur_retour, (20,482,180,55), 0) # avec : x,y, longueur, Epaisseur
        pygame.draw.rect(fenetre,(255,255,255), (20,482,180,55), 2)
        text = font.render("RETOUR", 1, (255, 255, 255))
    # Et voici le texte :
        fenetre.blit(text, (48,492))

    # 2) Voici le bouton suivant, et son cadre:
        pygame.draw.rect(fenetre,couleur_suivant, (598,482,180,55), 0) # avec : x,y, longueur, Epaisseur
        pygame.draw.rect(fenetre,(255,255,255), (598,482,180,55), 2)
        text = font.render("SUIVANT", 1, (255, 255, 255))

    # Et voici le texte :
        fenetre.blit(text, (622,492))

#---------------------------



        for event in pygame.event.get():

            if event.type == QUIT:
                return 0, 0, 0

            if event.type == MOUSEMOTION:

                if (event.pos[0] >= 20)  and (event.pos[0]<= 200) and (event.pos[1] >= 482)  and (event.pos[1] <= 537) :
                    couleur_retour = (127,35,128)

                elif (event.pos[0] >= 598)  and (event.pos[0]<= 778) and (event.pos[1] >= 482)  and (event.pos[1] <= 537) :
                    couleur_suivant = (127,35,128)

                else:
                    couleur_retour = (30,127,203)
                    couleur_suivant = (167,103,38)

            if event.type == MOUSEBUTTONDOWN and event.button == 1 :
                couleur_rect1 = 0
                couleur_rect2 = 0
                couleur_rect3 = 0
                couleur_rect4 = 0
                couleur_rect5 = 0
                couleur_rect6 = 0

                if (event.pos[0] >= 110)  and (event.pos[0]<= 257) and (event.pos[1] >= 113)  and (event.pos[1] <= 238):
                    couleur_rect1 = (198,8,0)
                    select = 1
                    fondchoix = "image/backgrounds/backmap-dune.png"
                    mapchoix = "image/maps/map-dune.png"

                elif (event.pos[0] >= 326)  and (event.pos[0]<= 473) and (event.pos[1] >= 113)  and (event.pos[1] <= 238):
                    couleur_rect2 = (198,8,0)
                    select = 2
                    fondchoix = "image/backgrounds/backmap-foret.png"
                    mapchoix = "image/maps/map-foret.png"

                elif (event.pos[0] >= 541)  and (event.pos[0]<= 689) and (event.pos[1] >= 113)  and (event.pos[1] <= 238):
                    couleur_rect3 = (198,8,0)
                    select = 3
                    fondchoix = "image/backgrounds/backmap-lune.png"
                    mapchoix = "image/maps/map-lune.png"
    #Rangee 2 88 devient 238 (+150 en y)

                elif (event.pos[0] >= 110)  and (event.pos[0]<= 257) and (event.pos[1] >= 306)  and (event.pos[1] <= 431):
                    couleur_rect4 = (198,8,0)
                    select = 4
                    fondchoix = "image/backgrounds/backmap-tunnel.png"
                    mapchoix = "image/maps/map-tunnel.png"

                elif (event.pos[0] >= 326)  and (event.pos[0]<= 473) and (event.pos[1] >= 306)  and (event.pos[1] <= 431):
                    couleur_rect5 = (198,8,0)
                    select = 5
                    fondchoix = "image/backgrounds/backmap-mars.png"
                    mapchoix = "image/maps/map-mars.png"

                elif (event.pos[0] >= 541)  and (event.pos[0]<= 689) and (event.pos[1] >= 306)  and (event.pos[1] <= 431):
                    couleur_rect6 = (198,8,0)
                    select = 6
                    fondchoix = "image/backgrounds/backmap-manif.png"
                    mapchoix = "image/maps/map-manif.png"
#----------------
                #bouton retour
                elif (event.pos[0] >= 20)  and (event.pos[0]<= 200) and (event.pos[1] >= 482)  and (event.pos[1] <= 537):
                    return 1, 0, 0
                #bouton suivant
                elif (event.pos[0] >= 598)  and (event.pos[0]<= 778) and (event.pos[1] >= 482)  and (event.pos[1] <= 537):
                    return 3, fondchoix, mapchoix #jouer
#----------------



      # Dessin des rectangles autour des menus


        pygame.draw.rect(fenetre,couleur_rect1, (107,110,156,134), 5)
        pygame.draw.rect(fenetre,couleur_rect2, (323,110,156,134), 5)
        pygame.draw.rect(fenetre,couleur_rect3, (539,110,156,134), 5)
        pygame.draw.rect(fenetre,couleur_rect4, (107,303,156,134), 5)
        pygame.draw.rect(fenetre,couleur_rect5, (323,303,156,134), 5)
        pygame.draw.rect(fenetre,couleur_rect6, (539,303,156,134), 5)


        pygame.display.flip()


#---------------------------------------------------------------------------------------
#Nouvelle fonction
#---------------------------------------------------------------------------------------


def menureglage():
    #initialisation variables
    couleur_retour = (30,127,203)
    couleur_suivant = (167,103,38)
    # Initialisation de la fenetre d'affichage
    pygame.display.set_caption("Mountain Domination - Réglages")

    # Remplissage de l'arriere-plan
    fond = pygame.image.load("image/backgrounds/backgroundmenureglages.png").convert()

   #Police des boutons textes
    font = pygame.font.Font("police.ttf", 26)

    sliderequipe = Slider(296, 127, 1, 5, 2) #Slider(posx, posy, valeurmini, valeurmaxi, valeur)
    slidervie = Slider(296, 184, 50, 200, 100)
    sliderduree = Slider(296, 239, 10, 80, 60)

    bouton1 = 1
    bouton2 = 1

    skin1 = "image/personnages/skinred1.png"
    skin2 = "image/personnages/skinblue1.png"

    affiche1 = pygame.image.load("image/boutonsmenu/btred1.png").convert_alpha()
    affiche2 = pygame.image.load("image/boutonsmenu/btblue1.png").convert_alpha()

    # Boucle infinie
    while 1:

        # Blitter le tout dans la fenetre
        fenetre.blit(fond, (0, 0))

    #Boutons retour (1) et suivant (2)

     # 1) Voici le bouton retour, et son cadre :
        pygame.draw.rect(fenetre,couleur_retour, (20,482,180,55), 0) # avec : x,y, longueur, Epaisseur
        pygame.draw.rect(fenetre,(255,255,255), (20,482,180,55), 2)
        text = font.render("RETOUR", 1, (255, 255, 255))
    # Et voici le texte :
        fenetre.blit(text, (48,492))

    # 2) Voici le bouton suivant, et son cadre:
        pygame.draw.rect(fenetre,couleur_suivant, (598,482,180,55), 0) # avec : x,y, longueur, Epaisseur
        pygame.draw.rect(fenetre,(255,255,255), (598,482,180,55), 2)
        text = font.render("SUIVANT", 1, (255, 255, 255))

    # Et voici le texte :
        fenetre.blit(text, (622,492))

        fenetre.blit(affiche1, (198, 358))
        fenetre.blit(affiche2, (475, 358))



#---------------------------

        for event in pygame.event.get():

            if event.type == QUIT:
                return 0, 0, 0, 0, 0, 0

            if event.type == MOUSEMOTION:

                if (event.pos[0] >= 20)  and (event.pos[0]<= 200) and (event.pos[1] >= 482)  and (event.pos[1] <= 537) :
                    couleur_retour = (127,35,128)

                elif (event.pos[0] >= 598)  and (event.pos[0]<= 778) and (event.pos[1] >= 482)  and (event.pos[1] <= 537) :
                    couleur_suivant = (127,35,128)

                else:
                    couleur_retour = (30,127,203)
                    couleur_suivant = (167,103,38)

            if event.type == MOUSEBUTTONDOWN and event.button == 1 :
                if (event.pos[0] >= 198)  and (event.pos[0]<= 298) and (event.pos[1] >= 358)  and (event.pos[1] <= 458):
                    bouton1 += 1
                    if bouton1 > 7 :
                        bouton1 = 1
                    affiche1 = pygame.image.load("image/boutonsmenu/btred"+str(bouton1)+".png").convert_alpha()
                    skin1 = "image/personnages/skinred"+str(bouton1)+".png"


                if (event.pos[0] >= 475)  and (event.pos[0]<= 575) and (event.pos[1] >= 358)  and (event.pos[1] <= 458):
                    bouton2 += 1
                    if bouton2 > 7 :
                        bouton2 = 1
                    affiche2 = pygame.image.load("image/boutonsmenu/btblue"+str(bouton2)+".png").convert_alpha()
                    skin2 = "image/personnages/skinblue"+str(bouton2)+".png"
#----------------
                #bouton retour
                elif (event.pos[0] >= 20)  and (event.pos[0]<= 200) and (event.pos[1] >= 482)  and (event.pos[1] <= 537):
                    return 2, 0, 0, 0, 0, 0
                #bouton suivant
                elif (event.pos[0] >= 598)  and (event.pos[0]<= 778) and (event.pos[1] >= 482)  and (event.pos[1] <= 537):
                    return 4, skin1, skin2, sliderequipe.valeur, slidervie.valeur, sliderduree.valeur #jouer

                sliderequipe.clic(event)
                slidervie.clic(event)
                sliderduree.clic(event)
#----------------
        sliderequipe.affiche(fenetre)
        slidervie.affiche(fenetre)
        sliderduree.affiche(fenetre)

        pygame.display.flip()

#---------------------------------------------------------------------------------------
#Class
#---------------------------------------------------------------------------------------


class Slider:
    def __init__(self, x, y, mini, maxi, valeur):
        self.x = x
        self.y = y
        self.maxi = maxi
        self.mini = mini
        self.valeur = valeur
        self.font = pygame.font.Font(None, 35)

    def clic(self, event):
        if (event.pos[0] >= self.x)  and (event.pos[0]<= self.x+200) and (event.pos[1] >= self.y)  and (event.pos[1] <= self.y+15):
            self.valeur = int((self.maxi-self.mini)*(event.pos[0]-self.x)/200)+self.mini

    def affiche(self, fenetre):
        pygame.draw.rect(fenetre, (127, 106, 0), (self.x, self.y, 200, 15), 0)
        pygame.draw.rect(fenetre, (255, 216, 0), ((self.valeur-self.mini)*200/(self.maxi-self.mini) + self.x, self.y, 15, 15), 0)
        texte = self.font.render(str(self.valeur), 1, (0,0,0))
        fenetre.blit(texte, (self.x+215,self.y-5))