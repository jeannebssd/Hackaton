import numpy as np
import math 
import random as rd

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
    return the list that contain the aleatory the top-left coordinate of the room, the length L and width l of the room
    '''
    L = rd.randint(1, 10) #longueur de la chambre
    l = rd.randint(1, 10) #largeur de la chambre
    x, y = rd.randint(1, 600-L), rd.randint(1, 600-l)
    return[[x,y], L, l]
        
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
    k = rd.randint(2,10)   # on considère que l'on a a minima 2 salles


def genere_salle():
    point, L, l = (-1,2), 4, 5     #room_information()
    M = np.array(L*[l*["."]])      # M est la matrice représentant la salle en question
                                   # elle est initialement pleine de points

    # génération des murs

    for i in range(L-1):
        M[i][0] = '|'
        M[i,-1] = '|'
    for j in range(l):
        M[0,j] = '-'
        M[-1,j] = '-'

    return M

print(genere_salle())






pg.quit()