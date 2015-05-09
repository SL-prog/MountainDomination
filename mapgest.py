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

    #Chargement de la montagne + mask + rect
    decor = pygame.sprite.Sprite()
    decor.image = pygame.image.load("image/mapcopie.png").convert_alpha()
    decor.rect = decor.image.get_rect()
    decor.rect.topleft = 0,0
    decor.mask = pygame.mask.from_surface(decor.image)

    #Chargement du rectangle projectile + mask + rect
    projectile = pygame.sprite.Sprite()
    projectile.image = pygame.image.load("image/armes/prj1.png").convert_alpha()
    projectile.rect = projectile.image.get_rect()
    projectile.mask = pygame.mask.from_surface(projectile.image)

    #generation des personnages :
    vies1 = [viemax]*nombre_perso #on donne de la vie a chaque perso
    vies2 = [viemax]*nombre_perso

    rouge = [0]*nombre_perso
    bleu = [0]*nombre_perso
    #creer les objets personnages
    for rang in range(nombre_perso):
        rouge[rang] = players.Player(rang, decor, projectile, skin1, randint(100, 700), 50, viemax, "red", tombe1)
        bleu[rang] = players.Player(rang, decor, projectile, skin2, randint(100, 700), 50, viemax, "blue", tombe2)

    return fond, decor, rouge, bleu, vies1, vies2


def mapMAJ(nombre_perso, rouge, bleu, ximpact, yimpact, arme, fenetre):
    if arme == 1:
        rayon = 45
        fenetre.blit(expl1,(ximpact-45,yimpact-45))
    if arme == 2:
        rayon = 65
        fenetre.blit(expl2,(ximpact-65,yimpact-65))
    pygame.display.flip()

    mapmaj = Image.open("image/mapcopie.png")
    draw = ImageDraw.Draw(mapmaj)
    #cercle transparent
    draw.ellipse((ximpact-rayon, yimpact-rayon, ximpact+rayon, yimpact+rayon), fill=(0, 0, 0, 0))
    mapmaj.save("image/mapcopie.png", 'PNG')

    #mettre a jour la map
    decor = pygame.sprite.Sprite()
    decor.image = pygame.image.load("image/mapcopie.png").convert_alpha()
    decor.rect = decor.image.get_rect()
    decor.rect.topleft = 0,0
    decor.mask = pygame.mask.from_surface(decor.image)

    for rang in range(nombre_perso):
        rouge[rang].decor = decor
        bleu[rang].decor = decor

    return decor