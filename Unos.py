import math
from Kretanje import *

f = open("podaci.txt", "w")
f.write('')

def Unos(brzinaStaraX,brzinaStaraY,playerX, playerY):
    dt = 0.01
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
    Ax, Ay = Ubrzanje(Gas, Kocnica, VolanRadian)
    brzinaX, brzinaY = Brzina(brzinaStaraX, brzinaStaraY, Ax, Ay, dt, playerX, playerY)
    Xx, Xy = Sledeca_Pozicija(brzinaX, brzinaY, dt, playerX, playerY)



    f.write((gas + ", " + kocnica + ", " + volan + "\t" + str(brzinaX) + ", " + str(
        brzinaY) + ", " + ", " + str(brzinaStaraX) + ", " + str(brzinaStaraY) + ", " + ", " + str(
        float(playerX)) + ", " + str(float(playerY)) + ", " + str(float(dt)) + "\n"))
    print((gas + ", " + kocnica + ", " + volan + "\t" + str(brzinaX) + ", " + str(brzinaY) + ", " + str(
        brzinaStaraX) + ", " + str(brzinaStaraY) + ", " + str(float(playerX)) + ", " + str(
        float(playerY)) + ", " + str(float(dt)) + "\n"))
    return Xx, Xy, brzinaX, brzinaY
