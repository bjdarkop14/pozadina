# This is an example that uses pygame.draw.rect:
import os, sys
import random
import math
import pygame
from pygame.locals import *
pygame.init()
APPLICATION_x_size = 500
APPLICATION_y_size = 400
start_x = 170       #x kordinata pocetnog bloka
start_y = 260       #y kordinata pocetnog bloka
x_size = 50         #duzina bloka
y_size = 30         #visina bloka

screen = pygame.display.set_mode((APPLICATION_x_size, APPLICATION_y_size))
pygame.display.set_caption('Random teren')
pygame.mouse.set_visible(True)
#pygame.mouse.set_visible(False)
black_square_that_is_the_size_of_the_screen = pygame.Surface(screen.get_size())
black_square_that_is_the_size_of_the_screen.fill((0, 0, 0))
screen.blit(black_square_that_is_the_size_of_the_screen, (0, 0))
pygame.display.flip()

# a color can be: (0 to 255, 0 to 255, 0 to 255)
My_light_blue_color = (190, 190, 255)
x = start_x
y = start_y
# "pygame.draw.rect(screen, Color, (x, y, x_size, y_size))"
pygame.draw.rect(screen, My_light_blue_color, (x, y, x_size, y_size))
# Weeee = True
# while Weeee:
while y > 0:
    q = random.randint(0,1)             #bira da li ce ici levo ili desno(0 - levo, 1 - desno
    if q == 0:
            x = x-35
            y = y-30
            pygame.draw.rect(screen, My_light_blue_color, (x, y, x_size, y_size))
    elif q == 1:
            x = x+35
            y = y-30
            pygame.draw.rect(screen, My_light_blue_color, (x, y, x_size, y_size))
pygame.display.flip()

   # if the 'X' button is pressed the window should close:
# Geesh = pygame.event.get()
# if len(Geesh) > 0:
#         if Geesh[0].type == QUIT: Weeee = False
## Once this line is reached the window should close

