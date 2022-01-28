# import pygame as pg
# from random import *

# def couloir(list, M):
#     res = []
#     for i in list:
#         for j in pourtour(i):
#             res.append(j)
#     for i in list:
#         k = randint(1,3)
#         for j in range(k):
#             l = randint(1, len(pourtour(i)))
#             if M[l[0], l[1]] != '+':
#                 M[l[0], l[1]] = '+'
#                 m = randint(0, len(list))
#                 if m != list.index(i):
#                     n = randint(1, len(pourtour(m)))
#                     if M[n[0], n[1]] != '+':
#                         M[n[0], n[1]] = '+'
#                         if pourtour(n)[0] > pourtour(i)[0]:
#                             for a in range(pourtour(i)[0], pourtour(n)[0]):
#                                 if (a, pourtour(i)[1]) not in res:
#                                     M[a, pourtour(i)[1]] = '#'
#                             if pourtour(n)[1] > pourtour(i)[1]:
#                                 for b in range(pourtour(i)[1], pourtour(n)[1]):
#                                     if b not in 
#                         else :
#                             for a in range(pourtour(n)[0], pourtour(i)[0]):
#                                 if (a, pourtour(n)[1]) not in res:
#                                     M[a, pourtour(n)[1]] = '#'
                        
import numpy as np
import math 
import random as rd
import pygame as pg
from random import randint
from itertools import product

from jeanne import room_information, pourtour


PV = 5   # nombre de vies initiales





# #1. Fond d'écran du jeu

# screen = pg.display.set_mode((600, 600)) #qui donnera du 20x20
# BLACK = (0, 0, 0)
# screen.fill(BLACK)


#L_couloir =  [[5,13-k] for k in range(5,10)] + [[5+k,8] for k in range(0,6)]


CHARACTER_COLOR = (128, 128, 0)
DIRECTIONS = {"DOWN": (0, 1), "UP": (0, -1), "RIGHT": (+1, 0), "LEFT": (-1, 0)}
W = 10
H = 10
X = 60
Y = 60

direction = DIRECTIONS["RIGHT"]

def draw_tile(x, y, color):
    """
    x and y in tiles coordinates
    translate into pixel coordinates for painting
    """
    rect = pg.Rect(x * W, y * H, W, H)
    pg.draw.rect(screen, color, rect)

pg.init()
screen = pg.display.set_mode((X * W, Y * H))
clock = pg.time.Clock()






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

def walls(info):
    point, L, l = info 
    x0, y0 = point
    mur_haut = [[x0+k,y0] for k in range(0,L)]
    mur_droit = [[x0+L,y0-k] for k in range(1,l+1)]
    mur_bas = [[x0+k,y0-l] for k in range(0,L+1)]
    mur_gauche = [[x0,y0-k] for k in range(0,l+1)]
    liste_hor = mur_haut + mur_bas 
    liste_ver = mur_gauche + mur_droit
    return liste_hor + liste_ver

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



# def draw_couloir(room1, room2):
#     for elt in pourtour(room1):
#         if couleur == (100,0,0) #si ya une porte 

def draw_couloir():
    mur_droit = [[5,13-k] for k in range(5,10)]
    mur_bas = [[5+k,8] for k in range(0,6)]
    for i in range (0,len(mur_bas)-1) : 
        elt = mur_bas[i]
        rect_mur = pg.Rect(elt[0]*30, elt[1]*30, 40, 10)
        pg.draw.rect(screen, (0,0,255), rect_mur)
    for i in range (1,len(mur_droit)) : 
        elt = mur_droit[i]
        rect_mur = pg.Rect(elt[0]*30, elt[1]*30, 10, 40)
        pg.draw.rect(screen, (0,0,255), rect_mur)

draw_couloir()

draw_door([10 ,10 - 2 ])
draw_door([2 + 3 ,4 ])


def move(character, direction):
    x, y = character
    dx, dy = direction
    return (x + dx, y + dy)

WHITE = (240, 240, 240)
BLACK = (0, 0, 0)
def draw_background():
    screen.fill(BLACK)


character_initial = (10, 15)
character = character_initial


murs = [(6,6), (6,7), (6,8), (6,9), (6,10),(6,11), (6,12), (21,6), (21,7), (21,8), (21,9), (21,10),(21,11), (21,12),
         (7,6), (8,6), (9,6), (10,6), (11,6), (12,6), (13,6), (14,6), (15,6), (16,6), (17,6), (18,6), (19,6), (20,6), (21,6),
         (7,12), (8,12), (9,12), (10,12), (11,12), (12,12), (13,12), (14,12), (15,12), (16,12), (17,12), (18,12), (19,12), (20,12), (21,12),
         (30, 21), (31, 21), (32, 21), (33, 21), (34, 21), (35, 21), (36, 21), (37, 21), (38, 21), (39, 21),
         (30, 31), (31, 31), (32, 31), (33, 31), (34, 31), (35, 31), (36, 31), (37, 31), (38, 31), (39, 31),
         (30, 21), (30, 22), (30, 23), (30, 24), (30, 25), (30, 26), (30, 27), (30, 28), (30, 29), (30, 30), 
         (39, 21), (39, 22), (39, 23), (39, 24), (39, 25), (39, 26), (39, 27), (39, 28), (39, 29), (39, 30)]

corridor =  [[5,13-k] for k in range(5,10)] + [[5+k,8] for k in range(0,6)]

running = True
while running:

    clock.tick(15)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                direction = DIRECTIONS["DOWN"]
            elif event.key == pg.K_UP:
                direction = DIRECTIONS["UP"]
            elif event.key == pg.K_RIGHT:
                direction = DIRECTIONS["RIGHT"]
            elif event.key == pg.K_LEFT:
                direction = DIRECTIONS["LEFT"]
            elif event.key == pg.K_q:
                running = False
    
    new_character = move(character, direction)
    if new_character in murs:
        if new_character not in corridor:
            direction = (0, 0)
            print("Interdit de foncer dans le mur")
    elif character in corridor:
        if new_character not in (corridor[corridor.index(character)-1], corridor[corridor.index(character)+1]):
            direction = (0, 0)
            print("Interdit de quitter le couloir")

    K = (10, 20)   # coordonées du king
    KING_COLOR = (255, 248, 220)
    
    # combat avec le King

    if new_character != character:
        if new_character in [(K[0]-1, K[1]), (K[0]+1, K[1]), (K[0], K[1]-1), (K[0], K[1]+1)] :              # pour le combattre il faut aller dessus
            N = rd.randint(0,10)
            if N >=7:
                PV -=1
            pg.display.set_caption(f"Vies restantes : {PV}")
    
    if PV == 0:
        print(f"Game over")
        pg.quit()
        exit()
    
    if new_character == K:
        direction = (0, 0)

    # les potions

    invisible_potion = (20, 20)   # coordonées de la potion
    invisible_potion_color = (255, 20, 147)

    if new_character == invisible_potion:
        draw_tile(invisible_potion[0], invisible_potion[1], (0,0,0))
        print(f"Vous avez récupéré une **invisble_potion**")

    character = move(character, direction)
    draw_background()

    draw_tile(invisible_potion[0], invisible_potion[1], invisible_potion_color)
    direction = (0, 0)
    draw_tile(K[0], K[1], KING_COLOR)
    draw_room(info_1)
    draw_room(info_2)
    draw_couloir()
    draw_door([10 ,10 - 2 ])
    draw_door([2 + 3 ,4 ])  
    draw_tile(character[0], character[1], CHARACTER_COLOR)
    pg.display.set_caption(f"Vies restantes : {PV}")

    pg.display.update()

pg.quit()
