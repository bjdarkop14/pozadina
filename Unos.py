import math
from Kretanje import *

f = open("podaci.txt", "w")
f.write('')

def Unos(instrukcija, brzinaStaraX,brzinaStaraY,playerX, playerY):
    dt = 10
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


    f.write((gas + ", " + kocnica + ", " + volan + "\t" + str(brzinaX) + ", " + str(brzinaY) + ", " + ", " + str(brzinaStaraX) + ", " + str(brzinaStaraY) + ", " + ", " + str(float(playerX)) + ", " + str(float(playerY)) + ", " + str(float(dt)) + "\n"))
    print((gas + ", " + kocnica + ", " + volan + "\t" + str(brzinaX) + ", " + str(brzinaY) + ", " + str(brzinaStaraX) + ", " + str(brzinaStaraY) + ", " + str(float(playerX)) + ", " + str(float(playerY)) + ", " + str(float(dt)) + "\n"))
    return Xx, Xy, brzinaX, brzinaY
