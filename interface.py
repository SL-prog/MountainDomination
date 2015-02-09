#-------------------------------------------------------------------------------
# Name:        Interface utilisateur
#
# Author:      regisseur
#
# Licence:     <GNU GENERAL PUBLIC LICENSE>
#-------------------------------------------------------------------------------

#Importation des bibliotheques necessaires
import pygame
from pygame.locals import *

def interface(fenetre, arme1, arme2, chargement0, chargement1, chargement2, chargement3, chargement4, horloge, switch, chargement, tempsjeu):
#rectangle
    pygame.draw.rect(fenetre, (79, 125, 51), (0, 480, 640, 80), 0) #pixel(s)
    pygame.draw.rect(fenetre, (0, 0, 0), (1, 480, 638, 80), 5)

    fenetre.blit(arme1, (22,502))
    fenetre.blit(arme2, (67,502))

    if switch == 1 :
        xrectarme = 20
    else :
        xrectarme = 65

    pygame.draw.rect(fenetre, (0, 0, 0), (xrectarme, 500, 40, 40), 2)

    if chargement < 5 :
        fenetre.blit(chargement0, (140,498))
    if chargement >= 5 and chargement < 10 :
        fenetre.blit(chargement1, (140,498))
    if chargement >= 10 and chargement < 20 :
        fenetre.blit(chargement2, (140,498))
    if chargement >= 20 and chargement < 30 :
        fenetre.blit(chargement3, (140,498))
    if chargement >= 30 :
        fenetre.blit(chargement4, (140,498))

    fenetre.blit(horloge, (500,495))
