import math

def Brzina(brzinaStaraX, brzinaStaraY, Ax, Ay ,dt, X0x, X0y):
    if X0x == 194 and X0y == 375:
        brzinaX = Ax * dt
        brzinaY = Ay * dt
        return brzinaX, brzinaY
    else:
        brzinaX = brzinaStaraX + Ax * dt
        brzinaY = brzinaStaraY + Ay * dt
        return brzinaX, brzinaY

def Ubrzanje(Gas, Kocnica, Volan):
    Ax = (Gas - Kocnica) * math.cos(Volan)
    Ay = (Gas - Kocnica) * math.sin(Volan)
    return Ax, Ay

def Sledeca_Pozicija(brzinaX, brzinaY, dt,  X0x, X0y):

    Xx = X0x + brzinaX * dt
    Xy = X0y - brzinaY * dt
    return Xx, Xy


