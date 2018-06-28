from teren import Crtaj
import pygame
from Kretanje import *
import time
import math
pygame.init()

# clock = pygame.time.Clock() # load clock

f = open("podaci.txt", "w")
f.write('')
button = pygame.Rect(160, 450, 140, 32)



def main():
    done = False
    brzinaStaraX = 0
    brzinaStaraY = 0
    start_x = 170  # x kordinata pocetnog bloka
    start_y = 360  # y kordinata pocetnog bloka
    x_size = 50  # duzina bloka
    y_size = 30
    x = start_x
    y = start_y
    playerX = 194
    playerY = 375
    dt = 0.01
    while not done:
        #clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            Crtaj(x, y, x_size, y_size)
            # dugme
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 1 is the left mouse button, 2 is middle, 3 is right.
                if event.button == 1:
                    # `event.pos` is the mouse position.
                    if button.collidepoint(event.pos):

                        gas = input("Unesi gas: ")
                        print(gas)
                        Gas = float(gas)
                        kocnica = input("Unesi kocnicu: ")
                        print(kocnica)
                        Kocnica = float(kocnica)
                        volan = input("Unesi volan")
                        print(volan)
                        VolanStepen = float(volan)
                        VolanRadian = math.radians(VolanStepen)

                        Ax, Ay = Ubrzanje(Gas,Kocnica,VolanRadian)
                        brzinaX, brzinaY = Brzina(brzinaStaraX,brzinaStaraY, Ax, Ay, dt, playerX, playerY)
                        Xx, Xy = Sledeca_Pozicija(brzinaX, brzinaY, dt, playerX,playerY)
                        playerX = Xx
                        playerY = Xy

                        f.write((gas + ", " + kocnica + ", " + volan + "\t" + str(brzinaX) +", "+ str(brzinaY)+", " +  ", " + str(brzinaStaraX)+", "+str(brzinaStaraY) + ", " + ", " + str(float(playerX)) + ", " + str(float(playerY)) + ", " + str(float(dt)) + "\n"))
                        print((gas + ", " + kocnica + ", " + volan + "\t" + str(brzinaX) +", "+ str(brzinaY)+ ", " + str(brzinaStaraX)+", "+str(brzinaStaraY)  + ", " + str(float(playerX)) + ", " + str(float(playerY)) + ", " + str(float(dt)) + "\n"))

                        print(brzinaStaraX,brzinaStaraY)
                        brzinaStaraX=brzinaX
                        brzinaStaraY=brzinaY
                        print(brzinaStaraX,brzinaY)
if __name__ == '__main__':
        main()
        pygame.quit()