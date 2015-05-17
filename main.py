#-------------------------------------------------------------------------------
# Name:        Mountain Domination
#
# Author:      sl-prog et regisseur
#
# Licence:     <GNU GENERAL PUBLIC LICENSE>
#-------------------------------------------------------------------------------
mountaindomination = True
while mountaindomination: #boucle principale de Mountain Domination
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

  #musique menu
  sonmenu.play(-1) #-1 pour infini

  #BOUCLE menu
  menu = 1
  #menu2 = False
  while menu>0 and menu<4:
      if menu==1:
          menu = menuprincipal()
      if menu==2:
          menu, fondchoix, mapchoix = menumap()
      if menu==3:
          menu, fondchoix, mapchoix = menuediteur()
      if menu == 4:
          menu, skin1, skin2, nombre_perso, viemax, duree_tour = menureglage()
  #-------------------


  #TEST
  switch = 1
  chargement = 0

  if menu == 0: #arreter jeu
    mountaindomination = False
    #variable fin de la boucle de jeu
    jeu = False

  #si menu = 5 lancer le jeu
  if menu == 5:
      #arret musique menu
      sonmenu.stop()
      sonjeu.play(-1) #-1 pour infini
      #Ouverture de la fenetre Pygame
      pygame.display.set_caption(titre_fenetre)
      #initialisation de la map
      fond, decor, rouge, bleu, vies1, vies2 = mapinit(skin1, skin2, nombre_perso, viemax, fondchoix, mapchoix)
      tempsjeu = duree_tour
      #Rafraichissement/mise a jour de l'ecran
      pygame.display.flip()
      #Simule des appuis tres rapide sur la touche quand on la maintient
      pygame.key.set_repeat(1, 1) #(duree appui, temps entre chaque appui)
      tour, jeu, mountaindomination = passertour(fenetre, 2)

  #BOUCLE de jeu
  while jeu:
  #Quitter le jeu
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              jeu = False
              mountaindomination = False
  #Front montant appuis touche
          elif event.type == pygame.KEYDOWN:
              if event.key == pygame.K_ESCAPE:
                jeu = False
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
                  if chargement < 35:
                      chargement+=1
  #Test touche D
              if event.key == pygame.K_d:
                  debug=True

              if event.key == pygame.K_f:
                  angle = "+"
              if event.key == pygame.K_g:
                  angle = "-"

              if event.key == pygame.K_p: #passer tour
                  tempsjeu = 0

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
                  rouge[numerorouge].tir(chargement)
                  bleu[numerobleu].tir(chargement)
                  #decor = mapMAJ(nombre_perso, rouge, bleu, rouge[0].rect.x, rouge[0].rect.y, switch, fenetre)
                  chargement = 0
  #touche D
              if event.key == pygame.K_d:
                  debug=False

              if event.key == pygame.K_f:
                  angle = ""
              if event.key == pygame.K_g:
                  angle = ""

  #Gerer mouvement personnages - mettre a jour vie
      for rang in range(nombre_perso):
          rouge[rang].mouvement(tour, numerorouge, saut, gauche, droite, debug, angle, switch)
          bleu[rang].mouvement(tour, numerobleu, saut, gauche, droite, debug, angle, switch)
          vies1[rang] = rouge[rang].vie
          vies2[rang] = bleu[rang].vie

  #Afficher le fond du jeu
      fenetre.blit(fond, (0,0))

  #Afficher la montagne -- Creer class
      fenetre.blit(decor.image, decor.rect)


  #Afficher les personnages
      for rang in range(nombre_perso):
          rouge[rang].affiche(fenetre)
          bleu[rang].affiche(fenetre)

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

      #faire passer tour aux morts
      if (rouge[numerorouge].jouer and not(rouge[numerorouge].vivant)) or (bleu[numerobleu].jouer and not(bleu[numerobleu].vivant)):
        tempsjeu = 0

  #timer temps jeu
      if pygame.time.get_ticks() > seconde:
          tempsjeu-=1
          seconde = pygame.time.get_ticks() + tempsattente
      if tempsjeu == -1:
          saut, gauche, droite, angle = 0,0,0,"" #pour eviter de controler le suivant avec les commandes du precedent
          if tour == 2: #gerer tour de jeu
            numerorouge+=1
            if numerorouge == nombre_perso: #rester dans la liste de perso
                numerorouge = 0
            while rouge[numerorouge].vivant == False: #interdire aux morts de jouer
                numerorouge+=1
                if numerorouge == nombre_perso:
                    numerorouge = 0
          if tour == 2:
            numerobleu+=1
            if numerobleu == nombre_perso:
                numerobleu = 0
            while bleu[numerobleu].vivant == False:
                numerobleu+=1
                if numerobleu == nombre_perso:
                    numerobleu = 0

          tour, jeu, mountaindomination = passertour(fenetre, tour)
          tempsjeu = duree_tour

      #arreter le jeu si une equipe gagne
      if sum(vies1) == 0 or sum(vies2) == 0:
        sonjeu.stop()
        songagner.play(-1) #infini
        jeu, mountaindomination = gagner(vies1, vies2)

  #Rafraichissement/mise a jour de l'ecran
      pygame.display.flip()
  #Limitation de vitesse de la boucle
      pygame.time.Clock().tick(30)
  sonjeu.stop()
pygame.quit()
