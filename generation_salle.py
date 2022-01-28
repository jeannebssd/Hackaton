import numpy as np
import math 
import numpy.random as rd

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