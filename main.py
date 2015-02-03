#-------------------------------------------------------------------------------
# Name:        Epic Mountain Battle
#
# Author:      sl-prog
#
# Licence:     <GNU GENERAL PUBLIC LICENSE>
#-------------------------------------------------------------------------------

#Importation et initialisation de la bibliotheque Pygame
import pygame
from pygame.locals import *
pygame.init()

#Importation des autres programmes
from constantes import *
import menu
import mapgest
import players
import interface

#Ouverture de la fenetre Pygame
fenetre = pygame.display.set_mode((largeur_ecran, hauteur_ecran), RESIZABLE) #fenetre de 640*480
pygame.display.set_caption(titre_fenetre)
pygame.display.set_icon(pygame.image.load(icon))

#Chargement du fond
fond = pygame.image.load(background).convert()

#Chargement de la montagne + mask + rect
decor = pygame.sprite.Sprite()
decor.image = pygame.image.load(mountain).convert_alpha()
decor.rect = decor.image.get_rect()
decor.rect.topleft = -80, 300
decor.mask = pygame.mask.from_surface(decor.image)


#Chargement et collage des personnages - test - + mask
image = pygame.sprite.Sprite()
image.image = pygame.image.load(escargot_rouge).convert_alpha()
image.rect = image.image.get_rect()
image.rect.topleft = x_rouge, y_rouge
image.mask = pygame.mask.from_surface(image.image)

image_retourne = pygame.sprite.Sprite()
image_retourne.image = pygame.transform.flip(image.image, 1, 0)
image_retourne.rect = image_retourne.image.get_rect()
image_retourne.rect.topleft = x_rouge, y_rouge
image_retourne.mask = pygame.mask.from_surface(image_retourne.image)


rouge = players.Player(decor, image, image_retourne, image.image, image_retourne.image, image.rect.x, image.rect.y)
# perso_bleu = pygame.image.load(escargot_bleu).convert_alpha()
# fenetre.blit(perso_bleu, (100,300))

#Rafraichissement/mise a jour de l'ecran
pygame.display.flip()

#Simule des appuis tres rapide sur la touche quand on la maintient
pygame.key.set_repeat(1, 1) #(dure appui, temps entre chaque appui)

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
                sens_perso = False
                gauche = True
            elif event.key == pygame.K_RIGHT:
                sens_perso = True
                droite = True
#saut
            if event.key == pygame.K_SPACE:
                saut=True


#Front descendant appuis touche
        elif event.type == pygame.KEYUP:
#fin deplacement droite-gauche
            if event.key == pygame.K_LEFT:
                gauche = False
            elif event.key == pygame.K_RIGHT:
                droite = False
#fin saut
            if event.key == pygame.K_SPACE:
                saut=False

#Afficher le fond du jeu
    fenetre.blit(fond, (0,0))

#Afficher la montagne
    fenetre.blit(decor.image, decor.rect)

#Gerer mouvement personnages
    rouge.mouvement(vitesse_perso_x, vitesse_perso_y, gravite, saut, gauche, droite)

#Afficher les personnages - TEST
#    rouge.affiche(fenetre, sens_perso, image.rect)
    fenetre.blit(image.image, image.rect)
#Afficher sens - TEST
    if sens_perso==True:
        charsens = 'droite'
        couleursens=(0,255,0)
    else:
        charsens = 'gauche'
        couleursens = (255,0,0)
    font = pygame.font.Font(None, 50)
    textsens = font.render(charsens, 1, couleursens)
    fenetre.blit(textsens, (260,10))

#afficher l'etat de la collision entre les deux sprites - TEST
    test_collision = pygame.sprite.collide_mask(image, decor)
    collision_char = "Collision" if test_collision else "Pas collision"
    collision = font.render(collision_char, 1, (0,0,0))
    fenetre.blit(collision, (10,30))


#Rafraichissement/mise a jour de l'ecran
    pygame.display.flip()

#Limitation de vitesse de la boucle
    pygame.time.Clock().tick(30)

pygame.quit()