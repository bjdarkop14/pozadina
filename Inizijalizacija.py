def Inizijalizacija():
    pop = 30
    n = 3
    m = 30
    a = [0] * m
    for i in range(m):
        a[i] = [0] * n
    import random

    for i in range(pop):
        for j in range(n):
            if j == 2:
                a[i][j] = random.randint(0, 180)
            else:
                a[i][j] = random.randint(0, 100)

    for i in range(pop):
        print(a[i])

