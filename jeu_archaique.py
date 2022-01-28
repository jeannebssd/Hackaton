import numpy as np
import math 
import random as rd

import pygame as pg
from random import randint


pg.init()
clock = pg.time.Clock()

#1. Fond d'écran du jeu

screen = pg.display.set_mode((600, 600)) #qui donnera du 20x20
BLACK = (0, 0, 0)
screen.fill(BLACK)

info_1 = [[10,10], 3, 3]
info_2 = [[200,200], 30, 30]

def draw_room(info): 
    point, L, l = info
    
    #dessine les murs 
    x0, y0 = point
    liste = [[x0,y0]]
    mur_haut = [[x0+k,y0] for k in range(0,L)]
    mur_droit = [[x0+L,y0-k] for k in range(0,l)]
    mur_bas = [[x0+k,y0-l] for k in range(0,L)]
    mur_gauche = [[x0,y0-k] for k in range(0,l)]
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



# Pour savoir si le bonhomme est encore dans la classe 
def in_scope(tile):
    x, y = tile
    return 0 <= x < X and 0 <= y < Y


running = True
while running:

    clock.tick(15)
    pg.display.update()

pg.quit()