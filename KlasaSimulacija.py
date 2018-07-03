import random
import math
import numpy
import pygame
from Inizijalizacija import Inizijalizacija
class Simulacija:
    def __init__(self, Niz_Instrukcija, Blok):
        self.Niz_Instrukcija = Niz_Instrukcija
        self.Blok = Blok

    def Brzina(self, brzinaStara, a, dt):
        brzina = numpy.array([0, 0])
        for i in range(0, 24):
            if i == 0:
                brzina[0] = a[0] * dt
                brzina[1] = a[1] * dt
                return brzina
            else:
                brzina[0] = brzinaStara[0] + a[0] * dt
                brzina[1] = brzinaStara[1] + a[1] * dt
                return brzina

    def Ubrzanje(self, i):
        Ax = (self.Niz_Instrukcija[i][0] - self.Niz_Instrukcija[i][1]) * math.cos(math.radians(self.Niz_Instrukcija[i][2]))
        Ay = (self.Niz_Instrukcija[i][0] - self.Niz_Instrukcija[i][1]) * math.sin(math.radians(self.Niz_Instrukcija[i][2]))
        a = numpy.array([Ax, Ay])
        return a

    def Sledeca_Pozicija(self, brzina, dt, x0):

        Xx = x0[0] + brzina[0] * dt
        Xy = x0[1] - brzina[0] * dt
        x = numpy.array([Xx, Xy])
        return x

    def Trci(self):
        dt = 0.1
        Fit = 0
        StaraBrzina = numpy.array([0,0])
        x0 = numpy.array([170, 760])
        for i in range(0, 24):
            a = self.Ubrzanje(i)
            brzina = self.Brzina(StaraBrzina, a, dt)
            x = self.Sledeca_Pozicija(brzina, dt, x0)
            Fit += self.Fittness(x, self.Blok[i][0], self.Blok[i][1]) * self.Fittness(x, self.Blok[i][0], self.Blok[i][1])
            # print(str(self.Niz_Instrukcija[i][0]) + ", " + str(self.Niz_Instrukcija[i][1]) + ", " + str(self.Niz_Instrukcija[i][2])
            #       + ", " + str(x0) + ", " + str(x) + ", " + str(StaraBrzina ) + ", " + str(brzina) + ", " + str(a))
            x0 = x
            StaraBrzina = brzina

        return numpy.sqrt((Fit / 24))
    def Fittness(self, x, XBloka, YBloka):
        x1 = numpy.array([XBloka, YBloka])
        x2 = numpy.array([XBloka+50, YBloka+30])
        x0 = (x1 + x2)/2
        return numpy.sqrt(((x0-x)*(x0-x)))          #Vraca Euklitsku distancu

    #Buble sort
    def Sort(self, Niz_Fitnessa, Niz_Jedinki):
        for passnum in range(len(Niz_Fitnessa) - 1, 0, -1):
            for i in range(passnum):
                if Niz_Fitnessa[i] > Niz_Fitnessa[i + 1]:
                    temp = Niz_Fitnessa[i]
                    k = Niz_Jedinki[i]
                    Niz_Fitnessa[i] = Niz_Fitnessa[i + 1]
                    Niz_Jedinki[i] = Niz_Jedinki[i+1]
                    Niz_Fitnessa[i + 1] = temp
                    Niz_Jedinki[i+1] = k
        return Niz_Jedinki, Niz_Fitnessa


