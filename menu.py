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
    fenetre.blit(fond, (0,0))
    # Boucle d'evenements
    while 1:
      #Changement des couleurs des boutons du menu, si la souris se met dessus.
        for event in pygame.event.get():

            if event.type == QUIT:
                return 0

            if event.type == MOUSEMOTION:
                if (event.pos[0] >= 220)  and (event.pos[0]<= 400) and (event.pos[1] >= 285)  and (event.pos[1] <= 340) :
                    couleur_quitter = (127,35,128)

                elif (event.pos[0] >= 220)  and (event.pos[0]<= 400) and (event.pos[1] >= 185)  and (event.pos[1] <= 240) :
                    couleur_jouer = (127,35,128)
                else:
                    couleur_quitter = (30,127,203)
                    couleur_jouer = (167,103,38)

        #Passage au "second menu", si il y'a clic sur le bouton "jouer"

            if event.type == MOUSEBUTTONDOWN and event.button == 1 and (event.pos[0] >= 220)  and (event.pos[0]<= 400) and (event.pos[1] >= 185)  and (event.pos[1] <= 240):
                return 2


        #Sortie du jeu, si il y a clic sur le bouton "quitter"

            if event.type == MOUSEBUTTONDOWN and event.button == 1 and (event.pos[0] >= 220)  and (event.pos[0]<= 400) and (event.pos[1] >= 285)  and (event.pos[1] <= 340):
                return 0

    # Affichage du bouton Jouer et son texte
    # Voici le bouton, et son cadre :
        pygame.draw.rect(fenetre,couleur_quitter, (220,285,180,55), 0) # avec : x,y, longueur, Epaisseur
        pygame.draw.rect(fenetre,(255,255,255), (220,285,180,55), 2)
        text = font.render("QUITTER", 1, (255, 255, 255))
    # Et voici le texte :
        textpos = text.get_rect()
        textpos.centerx = fond.get_rect().centerx
        textpos.centery = fond.get_rect().centery
        fond.blit(text, textpos)
        fenetre.blit(text, (243,295))


    # Affichage du bouton QUITTER et son texte
    # Voici le bouton, et son cadre:
        pygame.draw.rect(fenetre,couleur_jouer, (220,185,180,55), 0) # avec : x,y, longueur, Epaisseur
        pygame.draw.rect(fenetre,(255,255,255), (220,185,180,55), 2)
        text = font.render("JOUER", 1, (255, 255, 255))

    # Et voici le texte :

        textpos = text.get_rect()
        textpos.centerx = fond.get_rect().centerx
        textpos.centery = fond.get_rect().centery
        fond.blit(text, textpos)
        fenetre.blit(text, (264,195))

    # Blitter le tout dans la fenetre
        fenetre.blit(fenetre, (0, 0))
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
    #chargement images boutons choix map
    map1 = pygame.image.load("image/boutonsmenus/menudune.png").convert()
    map2 = pygame.image.load("image/boutonsmenus/menuforet.png").convert()
    map3 = pygame.image.load("image/boutonsmenus/menulune.png").convert()
    map4 = pygame.image.load("image/boutonsmenus/menutunnel.png").convert()
    map5 = pygame.image.load("image/boutonsmenus/menumars.png").convert()
    map6 = pygame.image.load("image/boutonsmenus/menumanif.png").convert()

    # Initialisation de la fenetre d'affichage
    pygame.display.set_caption("Mountain Domination - Choix map")

    # Remplissage de l'arriere-plan
    fond = pygame.image.load("image/backgrounds/backgroundmenumap.png").convert()
    fenetre.blit(fond, (0,0))
   #Police des boutons textes
    font = pygame.font.Font("police.ttf", 26)

    # Boucle infinie
    while 1:
#---------------------------------
    # Affichage des boutons map
        fenetre.blit(map1, (20,90))
        fenetre.blit(map2, (240,90))
        fenetre.blit(map3, (460,90))
        fenetre.blit(map4, (20,240))
        fenetre.blit(map5, (240,240))
        fenetre.blit(map6, (460,240))
#-------------------------------------------

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

                if (event.pos[0] >= 20)  and (event.pos[0]<= 170) and (event.pos[1] >= 90)  and (event.pos[1] <= 218):
                    couleur_rect1 = (198,8,0)
                    select = 1
                    fondchoix = "image/backgrounds/backmap-dune.png"
                    mapchoix = "image/maps/map-dune.png"

                elif (event.pos[0] >= 240)  and (event.pos[0]<= 390) and (event.pos[1] >= 90)  and (event.pos[1] <= 218):
                    couleur_rect2 = (198,8,0)
                    select = 2
                    fondchoix = "image/backgrounds/backmap-foret.png"
                    mapchoix = "image/maps/map-foret.png"

                elif (event.pos[0] >= 460)  and (event.pos[0]<= 610) and (event.pos[1] >= 90)  and (event.pos[1] <= 218):
                    couleur_rect3 = (198,8,0)
                    select = 3
                    fondchoix = "image/backgrounds/backmap-lune.png"
                    mapchoix = "image/maps/map-lune.png"
    #Rangee 2 88 devient 238 (+150 en y)

                elif (event.pos[0] >= 20)  and (event.pos[0]<= 170) and (event.pos[1] >= 238)  and (event.pos[1] <= 366):
                    couleur_rect4 = (198,8,0)
                    select = 4
                    fondchoix = "image/backgrounds/backmap-tunnel.png"
                    mapchoix = "image/maps/map-tunnel.png"

                elif (event.pos[0] >= 240)  and (event.pos[0]<= 390) and (event.pos[1] >= 238)  and (event.pos[1] <= 366):
                    couleur_rect5 = (198,8,0)
                    select = 5
                    fondchoix = "image/backgrounds/backmap-mars.png"
                    mapchoix = "image/maps/map-mars.png"

                elif (event.pos[0] >= 460)  and (event.pos[0]<= 610) and (event.pos[1] >= 238)  and (event.pos[1] <= 366):
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
                    return 4, fondchoix, mapchoix #jouer
#----------------



      # Dessin des rectangles autour des menus


        pygame.draw.rect(fenetre,couleur_rect1, (18,88,154,132), 5)
        pygame.draw.rect(fenetre,couleur_rect2, (238,88,154,132), 5)
        pygame.draw.rect(fenetre,couleur_rect3, (458,88,154,132), 5)
        pygame.draw.rect(fenetre,couleur_rect4, (18,238,154,132), 5)
        pygame.draw.rect(fenetre,couleur_rect5, (238,238,154,132), 5)
        pygame.draw.rect(fenetre,couleur_rect6, (458,238,154,132), 5)


    # Blitter le tout dans la fenetre
        fenetre.blit(fenetre, (0, 0))

        pygame.display.flip()