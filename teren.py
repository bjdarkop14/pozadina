import os, sys
import random
import math
import pygame
import time
from pygame.locals import *
pygame.init()
APPLICATION_x_size = 500
APPLICATION_y_size = 500

# a color can be: (0 to 255, 0 to 255, 0 to 255)
My_light_blue_color = (190, 190, 255)
My_light_red_color = (182, 0, 0)
FONT = pygame.font.Font(None, 32)

screen = pygame.display.set_mode((APPLICATION_x_size, APPLICATION_y_size))
pygame.display.set_caption('Simulacija')
pygame.mouse.set_visible(False)
black_square_that_is_the_size_of_the_screen = pygame.Surface(screen.get_size())
black_square_that_is_the_size_of_the_screen.fill((0, 0, 0))
screen.blit(black_square_that_is_the_size_of_the_screen, (0, 0))
pygame.display.flip()



def CrtajIgraca(Surface, PlayerColor, playerX,playerY,Xx,Xy):
    pygame.draw.line(Surface,PlayerColor,(playerX,playerY),(Xx,Xy))

def Crtaj():
    start_x = 170  # x kordinata pocetnog bloka
    start_y = 360  # y kordinata pocetnog bloka
    x_size = 50  # duzina bloka
    y_size = 30 # sirina bloka
    x = start_x
    y = start_y
    playerX = 194
    playerY = 375
    pygame.draw.rect(screen, My_light_blue_color, (x, y, x_size, y_size))   #prvi blok

    player = pygame.Rect((playerX, playerY, 4, 4))              #pocetna pozicija igraca
    pygame.draw.rect(screen, My_light_red_color, player)
    pygame.display.update()

    #generisanje random mape
    while y > 0:
        q = random.randint(0, 8)             #bira da li ce ici levo ili desno(0 - levo, 1 - desno
        if q == 0:
            y = y-30
            pygame.draw.rect(screen, My_light_blue_color, (x, y, x_size, y_size))
        elif q == 1:
            x = x + 20
            y = y - 30
            pygame.draw.rect(screen, My_light_blue_color, (x, y, x_size, y_size))
        elif q == 2:
            x = x - 20
            y = y - 30
            pygame.draw.rect(screen, My_light_blue_color, (x, y, x_size, y_size))
        elif q == 3:
            x = x - 10
            y = y - 30
            pygame.draw.rect(screen, My_light_blue_color, (x, y, x_size, y_size))
        elif q == 4:
            x = x + 10
            y = y - 30
            pygame.draw.rect(screen, My_light_blue_color, (x, y, x_size, y_size))
        elif q == 5:
            x = x - 5
            y = y - 30
            pygame.draw.rect(screen, My_light_blue_color, (x, y, x_size, y_size))
        elif q == 6:
            x = x + 5
            y= y - 30
            pygame.draw.rect(screen, My_light_blue_color, (x, y, x_size, y_size))
        elif q == 7:
            x = x - 15
            y = y - 30
            pygame.draw.rect(screen, My_light_blue_color, (x, y, x_size, y_size))
        elif q == 8:
            x = x + 15
            y = y - 30
            pygame.draw.rect(screen, My_light_blue_color, (x, y, x_size, y_size))

pygame.display.flip()
