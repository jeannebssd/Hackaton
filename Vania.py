import pygame as pg
from random import *

def couloir(list, M):
    res = []
    for i in list:
        for j in pourtour(i):
            res.append(j)
    for i in list:
        k = randint(1,3)
        for j in range(k):
            l = randint(1, len(pourtour(i)))
            if M[l[0], l[1]] != '+':
                M[l[0], l[1]] = '+'
                m = randint(0, len(list))
                if m != list.index(i):
                    n = randint(1, len(pourtour(m)))
                    if M[n[0], n[1]] != '+':
                        M[n[0], n[1]] = '+'
                        if pourtour(n)[0] > pourtour(i)[0]:
                            for a in range(pourtour(i)[0], pourtour(n)[0]):
                                if (a, pourtour(i)[1]) not in res:
                                    M[a, pourtour(i)[1]] = '#'
                            if pourtour(n)[1] > pourtour(i)[1]:
                                for b in range(pourtour(i)[1], pourtour(n)[1]):
                                    if b not in 
                        else :
                            for a in range(pourtour(n)[0], pourtour(i)[0]):
                                if (a, pourtour(n)[1]) not in res:
                                    M[a, pourtour(n)[1]] = '#'
                        
