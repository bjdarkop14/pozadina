import random
import math
from Inizijalizacija import Inizijalizacija
class Jedinka:
    def __init__(jedinka):
        for i in range(0, 24):
            jedinka[i] = Inizijalizacija(random.randint(0,9))
            jedinka[i].Gas = Jedinka.VratiGas(jedinka[i])
            jedinka[i].Kocnica = Jedinka.VratiKOcnicu(jedinka[i])
            jedinka[i].Volan = Jedinka.VratiVolan(jedinka[i])

    def Brzina(jedinka,brzinaStaraX, brzinaStaraY, Ax, Ay, dt, X0x, X0y):
        if X0x == 194 and X0y == 375:
            brzinaX = Ax * dt
            brzinaY = Ay * dt
            return brzinaX, brzinaY
        else:
            brzinaX = brzinaStaraX + Ax * dt
            brzinaY = brzinaStaraY + Ay * dt
            return brzinaX, brzinaY

    def Ubrzanje(Jedinka):
        Jedinka.Ax = (Gas - Kocnica) * math.cos(Volan)
        Jedinka.Ay = (Gas - Kocnica) * math.sin(Volan)


    def Sledeca_Pozicija(Jedinka, brzinaX, brzinaY, dt, X0x, X0y):

        Jedinka.Xx = X0x + brzinaX * dt
        Jedinka.Xy = X0y - brzinaY * dt


    def VratiGas(self, instrukcija):
        for i in instrukcija:
            if i == 0:
                return instrukcija[0]

    def VratiKOcnicu(self,instrukcija):
        for i in  instrukcija:
            if i == 1:
                return instrukcija[1]
    def VratiVolan(self, instrukcija):
        for i in instrukcija:
            if i == 2:
                return instrukcija[2]

    def Trci(self, ):