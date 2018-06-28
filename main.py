from teren import Crtaj
import pygame
from Kretanje import *
import time
import math
pygame.init()

f = open("podaci.txt", "w")
f.write('')
button = pygame.Rect(160, 450, 140, 32)

def main():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            start_x = 170  # x kordinata pocetnog bloka
            start_y = 360  # y kordinata pocetnog bloka
            x_size = 50  # duzina bloka
            y_size = 30
            brzinaStara = 0
            x = start_x
            y = start_y
            playerX = 194
            playerY = 375
            FrameRate = 60
            dt = 1.0 / FrameRate
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

                        brzina = Brzina(brzinaStara, Gas, Kocnica, playerX, playerY)

                        Xx = playerX + brzina * dt
                        playerX = Xx
                        Xy = playerY + brzina * dt
                        playerY = Xy
                        f.write((gas + ", " + kocnica + ", " + volan + "\t" + str(brzina) + ", " + str(brzinaStara) + ", " + str(float(playerX)) + ", " + str(float(playerY)) + ", " + str(float(dt)) + "\n"))
                        print((gas + ", " + kocnica + ", " + volan + "\t" + str(brzina) + ", " + str(brzinaStara) + ", " + str(float(playerX)) + ", " + str(float(playerY)) + ", " + str(float(dt)) + "\n"))
                        brzinaStara=brzina

if __name__ == '__main__':
        main()
        pygame.quit()