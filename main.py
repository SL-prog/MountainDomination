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

#Importation des autres programmes
from constantes import *
from mapgest import *
import players
from interface import *
#-------------------
from menu import *

#BOUCLE menu
menu = 1
#menu2 = False
while menu>0 and menu<4:
    if menu==1:
        menu = menuprincipal()
    if menu==2:
        menu, fondchoix, mapchoix = menumap()
#    if menu == 3:
#        menu = menureglage()
#-------------------


#TEST
switch = 1
chargement = 0
tour = 1
nombre_perso = 2 #nombre de personnage par equipe
viemax = 100

#variable fin de la boucle principale
jeu = False
if menu == 4:
    jeu = True
    #Ouverture de la fenetre Pygame
    pygame.display.set_caption(titre_fenetre)
    #initialisation de la map
    fond, decor, rouge, bleu, vies1, vies2 = mapinit(nombre_perso, viemax, fondchoix, mapchoix)
    #Rafraichissement/mise a jour de l'ecran
    pygame.display.flip()
    #Simule des appuis tres rapide sur la touche quand on la maintient
    pygame.key.set_repeat(1, 1) #(duree appui, temps entre chaque appui)

#BOUCLE Principale
while jeu:
#Quitter le jeu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jeu = False
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

#Gerer mouvement personnages - ajouter impossibilité controle mort
    for rang in range(nombre_perso):
        if rang != numero:
            rouge[rang].mouvement(vitesse_perso_x, vitesse_perso_y, gravite, 0, 0, 0,  debug, vitesse_saut)
            bleu[rang].mouvement(vitesse_perso_x, vitesse_perso_y, gravite, 0, 0, 0, debug, vitesse_saut)
    if tour == 1:
        bleu[numero].mouvement(vitesse_perso_x, vitesse_perso_y, gravite, 0, 0, 0, debug, vitesse_saut)
    if tour == 2:
        rouge[numero].mouvement(vitesse_perso_x, vitesse_perso_y, gravite, 0, 0, 0, debug, vitesse_saut)

    if tour == 1:
        rouge[numero].mouvement(vitesse_perso_x, vitesse_perso_y, gravite, saut, gauche, droite, debug, vitesse_saut)
    if tour == 2:
        bleu[numero].mouvement(vitesse_perso_x, vitesse_perso_y, gravite, saut, gauche, droite, debug, vitesse_saut)


#Afficher le fond du jeu
    fenetre.blit(fond, (0,0))

#Afficher la montagne -- Creer class
    fenetre.blit(decor.image, decor.rect)

    print(numero)

#Afficher les personnages - TEST
    for rang in range(nombre_perso):
        if vies1[rang]>0:
            rouge[rang].affiche(fenetre, vies1[rang])
        if vies2[rang]>0:
            bleu[rang].affiche(fenetre, vies2[rang])

#Afficher sens - TEST
#    if sens_perso==True:
#        charsens = 'droite'
#        couleursens=(0,255,0)
#    else:
#        charsens = 'gauche'
#        couleursens = (255,0,0)
#    font = pygame.font.Font(None, 50)
#    textsens = font.render(charsens, 1, couleursens)
#    fenetre.blit(textsens, (370,10))

#Afficher l'interface
    interface(fenetre, switch, chargement, tempsjeu, tour, vies1, vies2)

#----------------------
#TEST BARRE CHARGEMENT
    chargement+=1
    if chargement == 35:
        chargement = 0

#TEST BARRE VIE
    vies2[0]+=1
    if vies2[0] == 200:
        vies2[0] = 0
#----------------------

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
