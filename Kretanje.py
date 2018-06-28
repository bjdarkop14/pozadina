import math
import pygame
import numpy
from Unos_podataka import *
from pygame.locals import *
import math

playerX = 194
playerY = 375
def Brzina(brzinaStara, Gas, Kocnica, X0x, X0y):
    if X0x == playerX & X0y == playerY:
        brzina = (Gas - Kocnica)
        return brzina
    else:
        brzina=brzinaStara+(Gas-Kocnica)
        return brzina




    # if Volan < 0:
    #     Ax = X0x - int((Gas - Kocnica)*math.cos(Volan))
    #     Ay = X0y - abs(int((Gas - Kocnica) * math.sin(Volan)))
    # if Kocnica > Gas:
    #
    # elif Volan > 0:
    #     Xx = int((Gas - Kocnica)*math.cos(Volan)) + X0x
    #     Xy = X0x - abs(int((Gas - Kocnica)*math.sin(Volan)))
    #
    # Xx = X0x
    # Xy = X0y

