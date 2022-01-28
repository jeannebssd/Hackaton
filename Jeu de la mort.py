import pygame as pg
from random import randint


score=0

pg.init()
clock = pg.time.Clock()

#1. Fond d'écran du jeu

screen = pg.display.set_mode((600, 600))
WHITE = (240, 240, 240)
screen.fill(WHITE)

#2. Jeu 

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




def nombre_salle():
    k = randint(2,10)   # on considère que l'on a a minima 2 salles


def genere_salle():
    



pg.quit()