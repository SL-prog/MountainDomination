#-------------------------------------------------------------------------------
# Name:        Mountain Domination
#
# Author:      sl-prog et regisseur
#
# Licence:     <GNU GENERAL PUBLIC LICENSE>
#-------------------------------------------------------------------------------

#Importation et initialisation de la bibliotheque Pygame
import pygame
from pygame.locals import *
pygame.init()
#Importation du module genereation aleatoire
from random import randint

#Importation des autres programmes
from constantes import *
from menu import *
import mapgest
import players
from interface import *

#TEST
switch = 1
chargement = 0
tour = 1

#-------------------

#BOUCLE menu
menu = 1
#menu2 = False
while menu>0 and menu<4:
    if menu==1:
        menu = menuprincipal()
    if menu==2:
        menu = menumap()
#    if menu == 3:
#        menu = menureglage()
if menu==0:
    pygame.quit()

#-------------------

#Ouverture de la fenetre Pygame
pygame.display.set_caption(titre_fenetre)
pygame.display.set_icon(pygame.image.load(icon))

#Chargement du fond
fond = pygame.image.load(background).convert()

#Chargement de la montagne + mask + rect -> creer class
decor = pygame.sprite.Sprite()
decor.image = pygame.image.load(mountain).convert_alpha()
decor.rect = decor.image.get_rect()
decor.rect.topleft = 0,0
decor.mask = pygame.mask.from_surface(decor.image)

#generation des personnages :
nombre_perso = 2 #nombre de personnage par equipe
vies1 = [viemax]*nombre_perso #on donne de la vie a chaque perso
vies2 = [viemax]*nombre_perso

rouge = [0]*nombre_perso
bleu = [0]*nombre_perso
#creer les objets personnages
for rang in range(nombre_perso):
    rouge[rang] = players.Player(decor, escargot_rouge, randint(100, 700), 50)
    bleu[rang] = players.Player(decor, escargot_bleu, randint(100, 700), 50)


#Rafraichissement/mise a jour de l'ecran
pygame.display.flip()

#Simule des appuis tres rapide sur la touche quand on la maintient
pygame.key.set_repeat(1, 1) #(duree appui, temps entre chaque appui)

#BOUCLE Principale
while not done:
#Quitter le jeu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
#Front montant appuis touche
        elif event.type == pygame.KEYDOWN:
#deplacement droite-gauche
            if event.key == pygame.K_LEFT:
                sens_perso = False #TEST
                gauche = True
            elif event.key == pygame.K_RIGHT:
                sens_perso = True #TEST
                droite = True
#saut
            if event.key == pygame.K_UP:
                saut=True
#switch arme
            if (event.key == pygame.K_s) and switch==2:
                switch=1
            elif (event.key == pygame.K_s) and switch==1:
                switch=2

            if event.key == pygame.K_SPACE:
                pass
#Test touche D
            if event.key == pygame.K_d:
                debug=True


#Front descendant appuis touche
        elif event.type == pygame.KEYUP:
#fin deplacement droite-gauche
            if event.key == pygame.K_LEFT:
                gauche = False
            elif event.key == pygame.K_RIGHT:
                droite = False
#fin saut
            if event.key == pygame.K_UP:
                saut=False

            if event.key == pygame.K_SPACE:
                pass
#touche D
            if event.key == pygame.K_d:
                debug=False

#Gerer mouvement personnages
    for rang in range(0, nombre_perso):
        if rang != numero:
            rouge[rang].mouvement(vitesse_perso_x, vitesse_perso_y, gravite, 0, 0, 0,  debug, vitesse_saut)
            bleu[rang].mouvement(vitesse_perso_x, vitesse_perso_y, gravite, 0, 0, 0, debug, vitesse_saut)

    if tour == 1:
        rouge[numero].mouvement(vitesse_perso_x, vitesse_perso_y, gravite, saut, gauche, droite, debug, vitesse_saut)
    if tour == 2:
        bleu[numero].mouvement(vitesse_perso_x, vitesse_perso_y, gravite, saut, gauche, droite, debug, vitesse_saut)


#Afficher le fond du jeu
    fenetre.blit(fond, (0,0))

#Afficher la montagne -- Creer class
    fenetre.blit(decor.image, decor.rect)

#Afficher les personnages - TEST
    for rang in  range(nombre_perso):
        rouge[rang].affiche(fenetre, vies1[rang])
        bleu[rang].affiche(fenetre, vies2[rang])

#Afficher sens - TEST
    if sens_perso==True:
        charsens = 'droite'
        couleursens=(0,255,0)
    else:
        charsens = 'gauche'
        couleursens = (255,0,0)
    font = pygame.font.Font(None, 50)
    textsens = font.render(charsens, 1, couleursens)
    fenetre.blit(textsens, (370,10))

#Afficher l'interface
    interface(fenetre, arme1, arme2, chargement0, chargement1, chargement2, chargement3, chargement4, horloge, switch, chargement, tempsjeu, tour, vies1, vies2)

#TEST BARRE CHARGEMENT
    chargement+=1
    if chargement == 35:
        chargement = 0

#TEST BARRE VIE
    vies2[0]+=1
    if vies2[0] == 200:
        vies2[0] = 0

#Rafraichissement/mise a jour de l'ecran
    pygame.display.flip()

#timer temps jeu
    if pygame.time.get_ticks() > seconde:
        tempsjeu-=1
        seconde = pygame.time.get_ticks() + 1000
    if tempsjeu == -1:
        if tour==1:
            tour=2
        else :
            tour=1
            numero+=1
            if numero == nombre_perso:
                numero = 0
        tempsjeu = duree_tour

#Limitation de vitesse de la boucle
    pygame.time.Clock().tick(30)

pygame.quit()
