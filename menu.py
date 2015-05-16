#-------------------------------------------------------------------------------
# Name:        Menu
#
# Author:      Bretton's power et regisseur
#
# Licence:     <GNU GENERAL PUBLIC LICENSE>
#-------------------------------------------------------------------------------

import pygame
from pygame.locals import *
from constantes import *

from PIL import Image, ImageDraw

def menuprincipal():
    # Initialisation de la fenetre d'affichage
    pygame.display.set_caption("Mountain Domination - Menu")

    # Remplissage de l'arriere-plan
    fond = pygame.image.load("image/backgrounds/backgroundmenu.png").convert()

    #Creation boutons retour-suivant
    boutonjouer = Bouton(309,246,"JOUER",(30,127,203)) #Bouton(x,y,texte,couleur)
    boutonquitter = Bouton(309,356,"QUITTER",(167,103,38))

    # Boucle d'evenements
    while 1:
        #afficher le fond
        fenetre.blit(fond, (0,0))
        #afficher les boutons:
        boutonjouer.affiche(fenetre)
        boutonquitter.affiche(fenetre)

      #Changement des couleurs des boutons du menu, si la souris se met dessus.
        for event in pygame.event.get():
            if event.type == QUIT:
                return 0

            #interagir avec les boutons
            boutonjouer.interaction(event)
            boutonquitter.interaction(event)
            #si on clique sur un bouton etat=true
            if boutonjouer.etat == True: #on analyse l'etat du bouton
                return 2
            if boutonquitter.etat == True:
                return 0

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
    select = 0
    fondchoix = "image/backgrounds/backmap-dune.png"
    mapchoix = "image/maps/map-dune.png"
    # Initialisation de la fenetre d'affichage
    pygame.display.set_caption("Mountain Domination - Choix map")

    # Remplissage de l'arriere-plan
    fond = pygame.image.load("image/backgrounds/backgroundmenumap.png").convert()

    #Creation boutons retour-suivant
    boutonretour = Bouton(20,482,"RETOUR",(30,127,203)) #Bouton(x,y,texte,couleur)
    boutonsuivant = Bouton(598,482,"SUIVANT",(167,103,38))
    boutonediteur = Bouton(310,482,"EDITEUR",(150,0,38))

    # Boucle infinie
    while 1:
        # Blitter le tout dans la fenetre
        fenetre.blit(fond, (0, 0))
        #afficher les boutons:
        boutonretour.affiche(fenetre)
        boutonsuivant.affiche(fenetre)
        boutonediteur.affiche(fenetre)

        for event in pygame.event.get():

            if event.type == QUIT:
                return 0, 0, 0

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

            #interagir avec les boutons
            boutonretour.interaction(event)
            boutonsuivant.interaction(event)
            boutonediteur.interaction(event)
            #si on clique sur un bouton
            if boutonretour.etat == True:
                return 1, 0, 0 #menu principal
            if boutonsuivant.etat == True:
                return 4, fondchoix, mapchoix #menu reglage
            if boutonediteur.etat == True:
                return 3, fondchoix, mapchoix #menu editeur

      # Dessin des rectangles autour des boutons de choix
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
    # Initialisation de la fenetre d'affichage
    pygame.display.set_caption("Mountain Domination - Réglages")

    # Remplissage de l'arriere-plan
    fond = pygame.image.load("image/backgrounds/backgroundmenureglages.png").convert()

    #Creation sliders
    sliderequipe = Slider(296, 127, 1, 5, 2) #Slider(posx, posy, valeurmini, valeurmaxi, valeur)
    slidervie = Slider(296, 184, 50, 200, 100)
    sliderduree = Slider(296, 239, 10, 80, 60)

    #Creation boutons retour-suivant
    boutonretour = Bouton(20,482,"RETOUR",(30,127,203)) #Bouton(x,y,texte,couleur)
    boutonsuivant = Bouton(598,482,"SUIVANT",(167,103,38))

    #Creation boutons choix de perso
    bouton1 = 1
    bouton2 = 1
    skin1 = "image/personnages/skinred1.png"
    skin2 = "image/personnages/skinblue1.png"
    affiche1 = pygame.image.load("image/boutonsmenu/btred1.png").convert_alpha()
    affiche2 = pygame.image.load("image/boutonsmenu/btblue1.png").convert_alpha()

    # Boucle infinie
    while 1:

        #afficher le fond
        fenetre.blit(fond, (0, 0))

        #afficher les boutons choix perso
        fenetre.blit(affiche1, (198, 358))
        fenetre.blit(affiche2, (475, 358))

        #afficher les boutons et les sliders:
        boutonretour.affiche(fenetre)
        boutonsuivant.affiche(fenetre)
        sliderequipe.affiche(fenetre)
        slidervie.affiche(fenetre)
        sliderduree.affiche(fenetre)


        for event in pygame.event.get():

            if event.type == QUIT:
                return 0, 0, 0, 0, 0, 0

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

                #permettre aux sliders de savoir si on clique dessus
                sliderequipe.clic(event)
                slidervie.clic(event)
                sliderduree.clic(event)

            #interagir avec les boutons
            boutonretour.interaction(event)
            boutonsuivant.interaction(event)
            #si on clique sur un bouton
            if boutonretour.etat == True:
                return 2, 0, 0, 0, 0, 0
            if boutonsuivant.etat == True:
                return 5, skin1, skin2, sliderequipe.valeur, slidervie.valeur, sliderduree.valeur #jouer

        pygame.display.flip()


#---------------------------------------------------------------------------------------
#Nouvelle fonction
#---------------------------------------------------------------------------------------

def menuediteur():
    # Initialisation de la fenetre d'affichage
    pygame.display.set_caption("Mountain Domination - Map Editeur")

    # Remplissage de l'arriere-plan
    fond = pygame.image.load("image/backgrounds/backgroundmenuediteur.png").convert()

    #Creation boutons retour-suivant
    boutonretour = Bouton(20,493,"RETOUR",(30,127,203)) #Bouton(x,y,texte,couleur)
    boutongenerer = Bouton(598,493,"GENERER",(167,103,38))

    #Creation boutons choix texture map et texture fond
    bouton1 = 1
    bouton2 = 1
    skin1 = "image/maps/skinmap1.png"
    skin2 = "image/backgrounds/skinfond1.png"
    affiche1 = pygame.image.load("image/boutonsmenu/btmap1.png").convert_alpha()
    affiche2 = pygame.image.load("image/boutonsmenu/btfond1.png").convert_alpha()
    affiche3 = pygame.image.load("image/boutonsmenu/btdelet1.png").convert_alpha()

    mapeditaffiche = pygame.image.load("image/maps/mapedit.png").convert_alpha()
    curseur = "rectangle"
    largeurcurseur,longueurcurseur = 50,50
    pygame.mouse.set_visible(0)

    mapedit = Image.open("image/maps/mapedit.png")

    draw = ImageDraw.Draw(mapedit)

    # Boucle infinie
    while 1:

        #afficher le fond
        fenetre.blit(fond, (0, 0))

        fenetre.blit(mapeditaffiche, (0,0))

        fenetre.blit(affiche1, (320, 483))
        fenetre.blit(affiche2, (404, 483))

        fenetre.blit(affiche3, (490, 502))

        #afficher les boutons:
        boutonretour.affiche(fenetre)
        boutongenerer.affiche(fenetre)

#---------------------------
        (xsouris, ysouris) = pygame.mouse.get_pos() #recuperer les coordonnees curseur

            #dessiner le curseur
        if curseur == "rectangle":
            pygame.draw.rect(fenetre,(255,0,0), (xsouris-(largeurcurseur/2),ysouris-(longueurcurseur/2),largeurcurseur,longueurcurseur), 0)
        if curseur == "ellipse":
            pygame.draw.ellipse(fenetre, (255,0,0), (xsouris-(largeurcurseur/2),ysouris-(longueurcurseur/2),largeurcurseur,longueurcurseur), 0)


        for event in pygame.event.get():

            if event.type == QUIT:
                return 0, 0, 0

            if event.type == MOUSEMOTION:
                if (event.pos[0] >= 490)  and (event.pos[0]<= 530) and (event.pos[1] >= 502)  and (event.pos[1] <= 542):
                    affiche3 = pygame.image.load("image/boutonsmenu/btdelet2.png").convert_alpha()
                else:
                    affiche3 = pygame.image.load("image/boutonsmenu/btdelet1.png").convert_alpha()


            if event.type == MOUSEBUTTONDOWN and event.button == 1 :
                if (event.pos[0] >= 320)  and (event.pos[0]<= 396) and (event.pos[1] >= 483)  and (event.pos[1] <= 559):
                    bouton1 += 1
                    if bouton1 > 4 :
                        bouton1 = 1
                    affiche1 = pygame.image.load("image/boutonsmenu/btmap"+str(bouton1)+".png").convert_alpha()
                    skin1 = "image/maps/skinmap"+str(bouton1)+".png"


                if (event.pos[0] >= 404)  and (event.pos[0]<= 480) and (event.pos[1] >= 483)  and (event.pos[1] <= 559):
                    bouton2 += 1
                    if bouton2 > 4 :
                        bouton2 = 1
                    affiche2 = pygame.image.load("image/boutonsmenu/btfond"+str(bouton2)+".png").convert_alpha()
                    skin2 = "image/backgrounds/skinfond"+str(bouton2)+".png"

                elif (event.pos[0] >= 490)  and (event.pos[0]<= 530) and (event.pos[1] >= 502)  and (event.pos[1] <= 542):
                    draw.rectangle((0,0,800,480), fill=(255,255,255,0))
                    mapedit.save("image/maps/mapedit.png", 'PNG')
                    mapeditaffiche = pygame.image.load("image/maps/mapedit.png").convert_alpha()

                #afficher modifier map selon curseur
                if (event.pos[0] >= 0)  and (event.pos[0]<= 800) and (event.pos[1] >= 0)  and (event.pos[1] <= 480):
                    if curseur == "rectangle":
                        draw.rectangle((xsouris-(largeurcurseur/2),ysouris-(longueurcurseur/2),xsouris+(largeurcurseur/2),ysouris+(longueurcurseur/2)), fill=(255,255,255))
                    elif curseur == "ellipse":
                        draw.ellipse((xsouris-(largeurcurseur/2), ysouris-(longueurcurseur/2), xsouris+(largeurcurseur/2), ysouris+(longueurcurseur/2)), fill=(255,255,255))
                    mapedit.save("image/maps/mapedit.png", 'PNG')
                    mapeditaffiche = pygame.image.load("image/maps/mapedit.png").convert_alpha()

            if event.type == MOUSEBUTTONDOWN and event.button == 3 : #clique droit
                #afficher modifier map selon curseur
                if (event.pos[0] >= 0)  and (event.pos[0]<= 800) and (event.pos[1] >= 0)  and (event.pos[1] <= 480):
                    if curseur == "rectangle":
                        draw.rectangle((xsouris-(largeurcurseur/2),ysouris-(longueurcurseur/2),xsouris+(largeurcurseur/2),ysouris+(longueurcurseur/2)), fill=(255, 255, 255, 0))
                    elif curseur == "ellipse":
                        draw.ellipse((xsouris-(largeurcurseur/2), ysouris-(longueurcurseur/2), xsouris+(largeurcurseur/2), ysouris+(longueurcurseur/2)), fill=(255, 255, 255, 0))
                    mapedit.save("image/maps/mapedit.png", 'PNG')
                    mapeditaffiche = pygame.image.load("image/maps/mapedit.png").convert_alpha()

            #changer taille curseur
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE) and (curseur == "rectangle"):
                    curseur = "ellipse"
                elif (event.key == pygame.K_SPACE) and (curseur == "ellipse"):
                    curseur = "rectangle"
                if (event.key == pygame.K_UP) and (longueurcurseur<100):
                    longueurcurseur+=2
                if (event.key == pygame.K_DOWN) and (longueurcurseur>=6):
                    longueurcurseur-=2
                if (event.key == pygame.K_RIGHT) and (largeurcurseur<100):
                    largeurcurseur+=2
                if (event.key == pygame.K_LEFT) and (largeurcurseur>=6):
                    largeurcurseur-=2

            #interagir avec les boutons
            boutonretour.interaction(event)
            boutongenerer.interaction(event)
            #si on clique sur un bouton
            if boutonretour.etat == True:
                pygame.mouse.set_visible(1)
                return 2, 0, 0
            if boutongenerer.etat == True:
                pygame.mouse.set_visible(1)
                font = pygame.font.Font(None, 35)
                text = font.render("GENERATION EN COURS...", 1, (255, 0, 0))
                fenetre.blit(text, (240,260))
                pygame.display.flip()
                mapchoix = generer(skin1)
                return 4, skin2, mapchoix

        pygame.display.flip()

#---------------------------------------------------------------------------------------
#Nouvelle fonction
#---------------------------------------------------------------------------------------
def generer(skinmap):
    mapedit = Image.open("image/maps/mapedit.png", 'r')
    skin = Image.open(skinmap,'r')
    mapgenere = Image.new('RGBA', (800, 480))

    for y in range(480):
        for x in range(800):

            if mapedit.getpixel((x,y)) != (255, 255, 255, 0):
                pixel = skin.getpixel((x,y))
                mapgenere.putpixel((x,y), pixel)

    mapfinale = "image/mapgenere.png"

    mapgenere.save(mapfinale, 'PNG')


    return mapfinale

#---------------------------------------------------------------------------------------
#Nouvelle Class
#---------------------------------------------------------------------------------------

class Bouton: #on definit la class bouton
    def __init__(self, x, y, texte, couleur): #on recupere des coordonnees, du texte, et une couleur
        #on initialise les variables du bouton :
        self.font = font = pygame.font.Font("police.ttf", 26) #police du bouton
        self.x = x
        self.y = y
        self.texte = texte
        self.tailletexte = (len(self.texte)*19) #nombre de lettres * 20 (largeur moyenne d'une lettre)
        self.texteaffiche = font.render(self.texte, 1, (255, 255, 255)) #defini le texte a afficher avec couleur et police
        self.couleur = couleur #couleur sans survol avec la souris
        self.couleuraffiche = self.couleur #couleur a afficher
        self.couleursurvol = (127,35,128) #couleur au survol avec la souris
        self.etat = False #etat initial = pas clic

    def interaction(self, event): #on definit la fonction interaction (avec la souris) du bouton, qui recupere la variable event
        #event permet de savoir exactement l'etat de la souris (et du clavier)
        #si on bouge la souris dessus le bouton:
        if event.type == MOUSEMOTION:
            #si la souris est sur le bouton:
            #event.pos[0] = coordonnee souris en x, event.pos[1] = coordonnee souris en y
            if (event.pos[0] >= self.x)  and (event.pos[0]<= self.x+180) and (event.pos[1] >= self.y)  and (event.pos[1] <= self.y+55):
                self.couleuraffiche = self.couleursurvol #la couleur a afficher change
            #sinon la souris n'est pas dessus:
            else:
                self.couleuraffiche = self.couleur #la couleur a afficher redevient la couleur de base

        #si on clique dessus le bouton:
        if event.type == MOUSEBUTTONDOWN and event.button == 1 : #correspond au clique gauche
                #si la souris est sur le bouton:
            if (event.pos[0] >= self.x)  and (event.pos[0]<= self.x+180) and (event.pos[1] >= self.y)  and (event.pos[1] <= self.y+55):
                self.etat = True #le bouton change d'etat et devient appuye

    def affiche(self, fenetre):
        #cadre des boutons:
        pygame.draw.rect(fenetre,self.couleuraffiche, (self.x, self.y, 180,55), 0) # avec : x,y, longueur, Epaisseur
        pygame.draw.rect(fenetre,(255,255,255), (self.x, self.y, 180,55), 2)

        #centrer le texte selon sa taille:
        fenetre.blit(self.texteaffiche, (self.x+int((180-self.tailletexte)/2),self.y+10))
        #pour centrer le texte, on prend la valeur entiere de la division (largeur bouton - largeur du texte) par 2

#---------------------------------------------------------------------------------------
#Nouvelle Class
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
        if (event.pos[0] >= self.x+200)  and (event.pos[0]<= self.x+215) and (event.pos[1] >= self.y)  and (event.pos[1] <= self.y+15):
            self.valeur = self.maxi

    def affiche(self, fenetre):
        pygame.draw.rect(fenetre, (127, 106, 0), (self.x, self.y, 215, 15), 0)
        pygame.draw.rect(fenetre, (255, 216, 0), ((self.valeur-self.mini)*200/(self.maxi-self.mini) + self.x, self.y, 15, 15), 0)
        texte = self.font.render(str(self.valeur), 1, (0,0,0))
        fenetre.blit(texte, (self.x+235,self.y-5))