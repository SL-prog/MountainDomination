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

def mapinit(nombre_perso, viemax, fondchoix, mapchoix):
    #Chargement du fond
    fond = pygame.image.load(fondchoix).convert()

    #Chargement de la montagne + mask + rect -> creer class
    decor = pygame.sprite.Sprite()
    decor.image = pygame.image.load(mapchoix).convert_alpha()
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
        rouge[rang] = players.Player(decor, escargot_rouge, randint(100, 700), 50)
        bleu[rang] = players.Player(decor, escargot_bleu, randint(100, 700), 50)

    return fond, decor, rouge, bleu, vies1, vies2