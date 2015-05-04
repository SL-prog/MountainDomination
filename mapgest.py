#-------------------------------------------------------------------------------
# Name:        Map gestionnaire
#
# Author:      sl-prog
#
# Licence:     <GNU GENERAL PUBLIC LICENSE>
#-------------------------------------------------------------------------------

import pygame
from pygame.locals import *
from constantes import *
import players
#Importation du module genereation aleatoire
from random import randint

from PIL import Image, ImageDraw

def mapinit(skin1, skin2, nombre_perso, viemax, fondchoix, mapchoix):

    #copie image map
    mapcopie = Image.open(mapchoix)
    mapcopie.save("image/mapcopie.png", 'PNG')

    #Chargement du fond
    fond = pygame.image.load(fondchoix).convert()

    #Chargement de la montagne + mask + rect -> creer class
    decor = pygame.sprite.Sprite()
    decor.image = pygame.image.load("image/mapcopie.png").convert_alpha()
    decor.rect = decor.image.get_rect()
    decor.rect.topleft = 0,0
    decor.mask = pygame.mask.from_surface(decor.image)

    #generation des personnages :
    vies1 = [viemax]*nombre_perso #on donne de la vie a chaque perso
    vies2 = [viemax]*nombre_perso

    rouge = [0]*nombre_perso
    bleu = [0]*nombre_perso
    #creer les objets personnages
    for rang in range(nombre_perso):
        rouge[rang] = players.Player(rang, decor, skin1, randint(100, 700), 50, "red")
        bleu[rang] = players.Player(rang, decor, skin2, randint(100, 700), 50, "blue")

    return fond, decor, rouge, bleu, vies1, vies2


def mapMAJ(nombre_perso, rouge, bleu, ximpact, yimpact, arme):
    if arme == 1:
        rayon = 45
    if arme == 2:
        rayon = 65

    mapmaj = Image.open("image/mapcopie.png")
    draw = ImageDraw.Draw(mapmaj)
    #cercle transparent
    draw.ellipse((ximpact-rayon, yimpact-rayon, ximpact+rayon, yimpact+rayon), fill=(0, 0, 0, 0))
    mapmaj.save("image/mapcopie.png", 'PNG')

    decor = pygame.sprite.Sprite()
    decor.image = pygame.image.load("image/mapcopie.png").convert_alpha()
    decor.rect = decor.image.get_rect()
    decor.rect.topleft = 0,0
    decor.mask = pygame.mask.from_surface(decor.image)

    for rang in range(nombre_perso):
        rouge[rang].decor = decor
        bleu[rang].decor = decor

    return decor