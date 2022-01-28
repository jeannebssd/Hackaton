import numpy as np
import math 
import random as rd

import pygame as pg
from random import randint


pg.init()
clock = pg.time.Clock()

#1. Fond d'écran du jeu

screen = pg.display.set_mode((600, 600))
BLACK = (0, 0, 0)
screen.fill(BLACK)

info_1 = [[100,100], 20, 10]
info_2 = [[200,200], 30, 30]

def pourtour(info):
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

def draw_room(info): 
    point, L, l = info
    
    #dessine les murs 
    x0, y0 = point
    liste = [[x0,y0]]
    mur_haut = [[x0+k,y0] for k in range(1,L)]
    mur_droit = [[x0+L,y0-k] for k in range(1,l)]
    mur_bas = [[x0+k,y0-l] for k in range(1,L)]
    mur_gauche = [[x0,y0-k] for k in range(1,l)]
    liste += mur_haut + mur_droit + mur_gauche + mur_bas 
    for elt in liste : 
        rect_mur = pg.Rect(elt[0]*30, elt[1]*30, 30, 30)
        pg.draw.rect(screen, (255,0,0), rect_mur)

    #on dessine les points
    for i in range (1,L-1): #on ne prend pas les murs en compte
        for j in range (1,l-1):
            rect_point = pg.Rect((x0+50*i)*30, (y0+50*j)*30, 30, 30)
            pg.draw.rect(screen, (0,255,0), rect_point)

draw_room(info_1)

while True:
    pass

pg.quit()