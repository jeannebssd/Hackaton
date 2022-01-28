import numpy as np
import math 
import numpy.random as rd

import pygame as pg
from random import randint


score=0

pg.init()
clock = pg.time.Clock()

#1. Fond d'écran du jeu

screen = pg.display.set_mode((600, 600))
BLACK = (0, 0, 0)
screen.fill(BLACK)

#2. Deplacement
def room_information():
    '''
    return the list of lists that contain the aleatory coords of the , based on the number 
    of box
    '''
    liste_surfaces = []
    for i in range (number_of_room):
        L = rd.randint(1, 10) #longueur de la chambre
        l = rd.randint(1, 10) #largeur de la chambre
        x, y = rd.randint(1, 600-L), rd.randint(1, 600-l)
        return([x,y], L, l)
        

def pourtour(room):
    """
    return the list of coordonnates of the walls, takes in argument the information on the room 
    """
    x0, y0 = room[0]
    L, l = room[1], room[2]
    liste = [[x0,y0]]
    mur_haut = [[x0+k,y0] for k in range(L)]
    mur_droit = [[x0+L,y0-k] for k in range(l)]
    mur_bas = [[x0+k,y0-l] for k in range(L)]
    mur_gauche = [[x0,y0-k] for k in range(l)]
    liste += mur_haut + mur_droit + mur_gauche + mur_bas
    return(liste)



running = True
while running:
    clock.tick(2)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
                # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_q:
                running = False
            if event.key == pg.K_i:
                direction=[0,-1]
            if event.key == pg.K_k:
                direction=[0,1]
            if event.key == pg.K_l:
                direction=[1,0]
            if event.key == pg.K_j:
                direction=[-1,0]




def number_room():
    k = randint(2,10)   # on considère que l'on a a minima 2 salles


def genere_salle():
    M = np.zeros()              # M est la matrice représentant la salle en question
    point, L, l = room_information()
    # génération des murs






pg.quit()