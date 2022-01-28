import numpy as np
import math 
import random as rd
import pygame as pg
from itertools import product

# def number_room():
#     k = rd.randint(2,10)   # on considère que l'on a a minima 2 salles


# def genere_salle():
#     point, L, l = (-1,2), 4, 5     #room_information()
#     M = np.array(L*[l*["."]])      # M est la matrice représentant la salle en question
#                                    # elle est initialement pleine de points

#     # génération des murs

#     for i in range(L-1):
#         M[i][0] = '|'
#         M[i,-1] = '|'
#     for j in range(l):
#         M[0,j] = '-'
#         M[-1,j] = '-'

#     return M

# print(genere_salle())

CHARACTER_COLOR = (128, 128, 0)
DIRECTIONS = {"DOWN": (0, 1), "UP": (0, -1), "RIGHT": (+1, 0), "LEFT": (-1, 0)}
W = 10
H = 10
X = 40
Y = 40

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

murs = []
# for i in rooms:
#     for j in pourtour(i):
#         murs.append(i)

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
   # if new_character in murs:
   #     if new_character not in corridor:
   #         direction = (0, 0)
   #         print("Interdit de foncer dans le mur")
   # elif character in corridor:
   #     if new_character not in (corridor[corridor.index(character)-1], corridor[corridor.index(character)+1]):
   #         direction = (0, 0)
   #         print("Interdit de quitter le couloir")
    character = move(character, direction)
    draw_background()
    draw_tile(character[0], character[1], CHARACTER_COLOR)
    direction = (0, 0)

    PV = 5   # nombre de vies initiales
    pg.display.set_caption(f"Vies restantes : {PV}")

    K = (10, 20)   # coordonées du king
    KING_COLOR = (255, 248, 220)
    draw_tile(K[0], K[1], KING_COLOR)

    # combat avec le King

    N = rd.randint(0,10)
    if N >=7:
        PV -=1
    print("Vous avez perdu face au King")


    pg.display.update()

pg.quit()



