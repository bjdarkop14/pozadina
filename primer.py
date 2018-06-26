import os, sys
import random
import math
import pygame
from Unos_podataka import *
from pygame.locals import *
pygame.init()
APPLICATION_x_size = 1000
APPLICATION_y_size = 400
start_x = 170       #x kordinata pocetnog bloka
start_y = 360       #y kordinata pocetnog bloka
x_size = 50         #duzina bloka
y_size = 30         #visina bloka

# a color can be: (0 to 255, 0 to 255, 0 to 255)
My_light_blue_color = (190, 190, 255)
My_light_red_color = (182, 0, 0)
Button_Color = (220, 220, 220)
FONT = pygame.font.Font(None, 32)

screen = pygame.display.set_mode((APPLICATION_x_size, APPLICATION_y_size))
pygame.display.set_caption('Random teren')
pygame.mouse.set_visible(True)
#pygame.mouse.set_visible(False)
black_square_that_is_the_size_of_the_screen = pygame.Surface(screen.get_size())
black_square_that_is_the_size_of_the_screen.fill((0, 0, 0))
screen.blit(black_square_that_is_the_size_of_the_screen, (0, 0))
pygame.display.flip()

x = start_x
y = start_y
# "pygame.draw.rect(screen, Color, (x, y, x_size, y_size))"
pygame.draw.rect(screen, My_light_blue_color, (x, y, x_size, y_size))
pygame.draw.rect(screen, My_light_red_color, (194, 375, 4, 4))

clock = pg.time.Clock()
input_box1 = InputBox(700, 20, 140, 32)
input_box2 = InputBox(700, 100, 140, 32)
input_box3 = InputBox(700, 180, 140, 32)
input_boxes = [input_box1, input_box2, input_box3]
done = False
f = open("podaci.txt", "w")
f.write('')
button = pygame.Rect(635, 296, 140, 32)

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

            #dugme
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 1 is the left mouse button, 2 is middle, 3 is right.
            if event.button == 1:
                # `event.pos` is the mouse position.
                if button.collidepoint(event.pos):
                    gas = input_box1.text.strip()
                    print(gas)
                    kocnica = input_box2.text.strip()
                    print(kocnica)
                    volan = input_box3.text.strip()
                    print(volan)
                    f.write(gas)
                    f.write(", ")
                    f.write(kocnica)
                    f.write(", ")
                    f.write(volan)
                    input_box1.text = ''
                    input_box2.text = ''
                    input_box3.text = ''

        pygame.draw.rect(screen, Button_Color, button)
        labelButton = FONT.render("Prodji",1,(0,0,0))
        screen.blit(labelButton,(650,300))
        pygame.display.update()

        for box in input_boxes:
            box.handle_event(event)

    for box in input_boxes:
        box.update()

    for box in input_boxes:
        box.draw(screen)
    # render text
    labelGas = FONT.render("Gas", 1, (255, 255, 0))
    screen.blit(labelGas, (600, 20))
    labelKocnica = FONT.render("Kocnica", 1, (255, 255, 0))
    screen.blit(labelKocnica, (600, 100))
    labelVolan = FONT.render("Volan", 1, (255, 255, 0))
    screen.blit(labelVolan, (600, 180))
    pg.display.flip()
    clock.tick(30)


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




