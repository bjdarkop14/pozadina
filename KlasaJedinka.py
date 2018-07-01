import random
import math
import pygame
from Inizijalizacija import Inizijalizacija
class Simulacija:
    def __init__(self, Niz_Instrukcija):
        self.Niz_Instrukcija = Niz_Instrukcija


    def Brzina(self, brzinaStaraX, brzinaStaraY, Ax, Ay, dt):
        for i in self.Niz_Instrukcija:
            if i == 0:
                brzinaX = Ax * dt
                brzinaY = Ay * dt
                return brzinaX, brzinaY
            else:
                brzinaX = brzinaStaraX + Ax * dt
                brzinaY = brzinaStaraY + Ay * dt
                return brzinaX, brzinaY

    def Ubrzanje(self, i):
        Ax = (self.Niz_Instrukcija[i][0] - self.Niz_Instrukcija[i][1]) * math.cos(math.radians(self.Niz_Instrukcija[i][2]))
        Ay = (self.Niz_Instrukcija[i][0] - self.Niz_Instrukcija[i][1]) * math.sin(math.radians(self.Niz_Instrukcija[i][2]))
        return Ax, Ay

    def Sledeca_Pozicija(self, brzinaX, brzinaY, dt, X0x, X0y):

        Xx = X0x + brzinaX * dt
        Xy = X0y - brzinaY * dt
        return Xx, Xy

    def Trci(self):
        dt = 1
        brzinaStaraX = 0
        brzinaStaray = 0
        X0x = 170
        X0y = 360
        for i in range(0,12):
            Ax, Ay = self.Ubrzanje(i)
            brzinaX, brzinaY  = self.Brzina(brzinaStaraX, brzinaStaray, Ax, Ay, dt)
            Xx, Xy = self.Sledeca_Pozicija(brzinaX, brzinaY, dt, X0x, X0y)
            X0x = Xx
            X0y = Xy
            print(str(self.Niz_Instrukcija[i][0]) + ", " + str(self.Niz_Instrukcija[i][1]) +", " +  str(self.Niz_Instrukcija[i][2]) +
                  ", " + str(X0x) + ", " + str(X0y) + ", " + str(Xx) + ", " + str(Xy) + ", " + str(brzinaX) +", " + str(brzinaY) +
                  ", " + str(Ax) + ", " + str(Ay))