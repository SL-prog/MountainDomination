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
from constantes import *

def interface(fenetre, switch, chargement, tempsjeu, tour, vies1, vies2):
#rectangle
    pygame.draw.rect(fenetre, (79, 125, 51), (0, 480, 800, 80), 0) #pixel(s)
    pygame.draw.rect(fenetre, (0, 0, 0), (1, 480, 798, 80), 5)

    equipe1 = sum(vies1)
    equipe2 = sum(vies2)
    totalvie = equipe1 + equipe2

    if totalvie != 0:
        pygame.draw.rect(fenetre, (255, 0, 0), (200, 498, ((400*equipe1)/totalvie), 44), 0)
        pygame.draw.rect(fenetre, (0, 0, 255), ((200+(400*equipe1)/totalvie), 498, ((400*equipe2)/totalvie), 44), 0)


    pygame.draw.rect(fenetre, (0, 0, 0), (200, 498, 400, 44), 2)


    font = pygame.font.Font(None, 30)
    if tour == 1 :
        joueur = 'Equipe 1'
        couleur = (255,0,0)

    else:
        joueur = 'Equipe 2'
        couleur = (0,0,255)

    tour = font.render(joueur, 1, couleur)

    fenetre.blit(tour, (685, 510)) #+160


    fenetre.blit(arme1, (22,502))
    fenetre.blit(arme2, (67,502))

    if switch == 1 :
        xrectarme = 20
    else :
        xrectarme = 65

    pygame.draw.rect(fenetre, (0, 0, 0), (xrectarme, 500, 40, 40), 2)

    if chargement < 5 :
        fenetre.blit(chargement0, (130,498))
    if chargement >= 5 and chargement < 10 :
        fenetre.blit(chargement1, (130,498))
    if chargement >= 10 and chargement < 20 :
        fenetre.blit(chargement2, (130,498))
    if chargement >= 20 and chargement < 30 :
        fenetre.blit(chargement3, (130,498))
    if chargement >= 30 :
        fenetre.blit(chargement4, (130,498))


    fenetre.blit(horloge, (617,495))
    font = pygame.font.Font(None, 40)
    temps = str(tempsjeu)
    temps = font.render(temps, 1, (0,0,0))
    if tempsjeu <= 9:
        xtemps = 636
    else:
        xtemps = 626
    fenetre.blit(temps, (xtemps,508))


def passertour(fenetre, tour):
    attendre = True
    jeu = True
    if tour==1:
        tour=2
        fenetre.blit(tourjoueur2, (0,130))
    else :
        tour=1
        fenetre.blit(tourjoueur1, (0,130))
    pygame.display.flip()
    while attendre==True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jeu = False
                attendre = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    attendre = False
    return tour, jeu



