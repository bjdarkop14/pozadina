import random

def RandomZaPopulaciju():
    a = [0] * 24
    for i in range(0, 24):
        a[i][0] = random.randint(0,100)
        a[i][1] = random.randint(0,100)
        a[i][2] = random.randint(0,180)





def Inizijalizacija(Skretanje):
    a = [0] * 24
    for i in range(0, 24):
        a[i] = [0]*3
    for i in range(0, 24):
        if Skretanje[i] == 0:
            a[i][0] = random.randint(0, 100)
            a[i][1] = random.randint(0, 100)
            a[i][2] = random.randint(0, 180)
        if Skretanje[i] == 1:
            a[i][0] = random.randint(0, 100)
            a[i][1] = random.randint(0, 100)
            a[i][2] = random.randint(0, 180)
        if Skretanje[i] == 2:
            a[i][0] = random.randint(0, 100)
            a[i][1] = random.randint(0, 100)
            a[i][2] = random.randint(0, 180)
        if Skretanje[i] == 3:
            a[i][0] = random.randint(0, 100)
            a[i][1] = random.randint(0, 100)
            a[i][2] = random.randint(0, 180)
        if Skretanje[i] == 4:
            a[i][0] = random.randint(0, 100)
            a[i][1] = random.randint(0, 100)
            a[i][2] = random.randint(0, 180)
        if Skretanje[i] == 5:
            a[i][0] = random.randint(0, 100)
            a[i][1] = random.randint(0, 100)
            a[i][2] = random.randint(0, 180)
        if Skretanje[i] == 6:
            a[i][0] = random.randint(0, 100)
            a[i][1] = random.randint(0, 100)
            a[i][2] = random.randint(0, 180)
        if Skretanje[i] == 7:
            a[i][0] = random.randint(0, 100)
            a[i][1] = random.randint(0, 100)
            a[i][2] = random.randint(0, 180)
        if Skretanje[i] == 8:
            a[i][0] = random.randint(0, 100)
            a[i][1] = random.randint(0, 100)
            a[i][2] = random.randint(0, 180)
    return a

