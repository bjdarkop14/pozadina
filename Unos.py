import math
from Kretanje import *

def Unos(instrukcija, brzinaStaraX,brzinaStaraY,playerX, playerY):
    dt = 7
    Gas = instrukcija[0]
    Kocnica = instrukcija[1]
    VolanStepen = instrukcija[2]
    VolanRadian = math.radians(VolanStepen)
    Ax, Ay = Ubrzanje(Gas, Kocnica, VolanRadian)
    brzinaX, brzinaY = Brzina(brzinaStaraX, brzinaStaraY, Ax, Ay, dt, playerX, playerY)
    Xx, Xy = Sledeca_Pozicija(brzinaX, brzinaY, dt, playerX, playerY)

    gas = str(Gas)
    kocnica = str(Kocnica)
    volan = str(VolanStepen)
    print((gas + ", " + kocnica + ", " + volan + "\t" + str(int(brzinaX)) + ", " + str(int(brzinaY)) + ", " + str(int(brzinaStaraX)) + ", " + str(int(brzinaStaraY)) + ", "  + str(int(playerX)) + ", " + str(int(playerY)) + ", " + str(int(Ax)) + ", " + str(int(Ay)) + "\n"))
    return Xx, Xy, brzinaX, brzinaY
