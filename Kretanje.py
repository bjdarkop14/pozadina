import math

playerX = 194
playerY = 375
def Brzina(brzinaStaraX, brzinaStaraY, Ax, Ay ,dt, X0x, X0y):
    if X0x == playerX and X0y == playerY:
        brzinaX = Ax * dt
        brzinaY = Ay * dt
        return brzinaX, brzinaY
    else:
        brzinaX = brzinaStaraX + Ax * dt
        brzinaY = brzinaStaraY + Ay * dt
        return brzinaX, brzinaY

def Ubrzanje(Gas, Kocnica, Volan):
    Ax = (Gas - Kocnica) * math.cos(Volan)
    Ay = (Gas - Kocnica) * math.cos(Volan)
    return Ax, Ay

def Sledeca_Pozicija(brzinaX, brzinaY, dt,  X0x, X0y):

    Xx = X0x + brzinaX * dt
    Xy = X0y - brzinaY * dt
    return Xx, Xy


