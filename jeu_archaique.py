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

info_1 = [[10,10], 3, 3] #rect de 3*3 
info_2 = [[2,4], 5, 2]

def draw_room(info): 
    point, L, l = info
    
    #dessine les murs 
    x0, y0 = point
    mur_haut = [[x0+k,y0] for k in range(0,L)]
    mur_droit = [[x0+L,y0-k] for k in range(1,l+1)]
    mur_bas = [[x0+k,y0-l] for k in range(0,L+1)]
    mur_gauche = [[x0,y0-k] for k in range(0,l+1)]
    liste_hor = mur_haut + mur_bas 
    liste_ver = mur_gauche + mur_droit
    for i in range (0,len(liste_hor)-1) : 
        elt = liste_hor[i]
        rect_mur = pg.Rect(elt[0]*30, elt[1]*30, 40, 10)
        pg.draw.rect(screen, (255,0,0), rect_mur)
    for i in range (1,len(liste_ver)) : 
        elt = liste_ver[i]
        rect_mur = pg.Rect(elt[0]*30, elt[1]*30, 10, 40)
        pg.draw.rect(screen, (255,0,0), rect_mur)

    #on dessine les points
    # for i in range (0,L-1): #on ne prend pas les murs en compte
    #     for j in range (0,l-1):
    #         pg.draw.circle(screen, (0,255,0), [(30*x0+i), (30*y0+j)], 3)


draw_room(info_1)
draw_room(info_2)

# def draw_door(room):
#     i,j = rd.randint()
#     rect_mur = pg.Rect(elt[0]*30, elt[1]*30, 10, 40)
#         pg.draw.rect(screen, (100,0,0), rect_mur)

def draw_door(coords):
    x,y = coords[0], coords[1]
    rect_mur = pg.Rect(x*30, y*30, 10, 10)
    pg.draw.rect(screen, (100,0,0), rect_mur)

draw_door([10 + 2 ,10])
draw_door([2,4 - 1])


# Pour savoir si le bonhomme est encore dans la classe 
def in_scope(tile):
    x, y = tile
    return 0 <= x < X and 0 <= y < Y


running = True
while running:

    clock.tick(15)
    pg.display.update()

pg.quit()