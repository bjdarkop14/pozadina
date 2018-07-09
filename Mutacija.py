import random
def Mutacija(Niz):
    for i in range(0,24):
        Niz[i][0] = Niz[i][0] + random.randint(-30,30)
        Niz[i][1] = Niz[i][1] + random.randint(-30,30)
        Niz[i][2] = Niz[i][2] + random.randint(-25,25)
    return Niz