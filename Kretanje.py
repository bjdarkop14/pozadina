import math

playerX = 194
playerY = 375
def Brzina(brzinaStara, Gas, Kocnica, X0x,X0y):
    if X0x == playerX and X0y == playerY:
        brzina = (Gas - Kocnica)
        return brzina
    else:
        brzina=brzinaStara+(Gas-Kocnica)
        if brzina<0:
            brzina = 0
        return brzina


def Sledeca_Pozicija(Volan, brzina, X0x, X0y):
    if Volan < 0:
        Xx = X0x - brzina * math.cos(Volan)
        Xy = X0y -  brzina* math.sin(Volan)
    elif Volan == 0:
        Xx = X0x
        Xy = X0y
    elif Volan > 0:
        Xx = brzina*math.cos(Volan) + X0x
        Xy = X0x - brzina*math.sin(Volan)

    return Xx,Xy


