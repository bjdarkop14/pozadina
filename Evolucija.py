import random
# from deap import base
# from deap import creator
# from deap import tools
from Inizijalizacija import *
from Sort import Sort
from KlasaSimulacija import *
from CrossOver import *
from Mutacija import *

def main():
    start_x = 170
    start_y = 760
    x = start_x
    y = start_y
    ix = 0
    Skretanje = [0] * 50
    Blok = [0]*50
    while ix < 24:
        q = random.randint(0, 9)                # bira da li ce ici levo ili desno(0 - levo, 1 - desno
        Skretanje[ix] = q
        if q == 0:
            y = y - 30
        elif q == 1:
            x = x + 20
            y = y - 30
        elif q == 2:
            x = x - 20
            y = y - 30
        elif q == 3:
            x = x - 10
            y = y - 30
        elif q == 4:
            x = x + 10
            y = y - 30
        elif q == 5:
            x = x - 5
            y = y - 30
        elif q == 6:
            x = x + 5
            y = y - 30
        elif q == 7:
            x = x - 15
            y = y - 30
        elif q == 8:
            x = x + 15
            y = y - 30
        Blok[ix] = numpy.array([x, y])
        ix += 1

    Niz_Jedinki = []
    Niz_Fitnessa = []

    f = open("podaci1.txt","w")
    Generacija = 100
    br_Jedinki = 20
    CrossPop = int(0.3 * br_Jedinki)
    NajboljiBr = int(0.4 * br_Jedinki)
    OstaliBr = int(0.3 * br_Jedinki)
    for i in range(0, br_Jedinki):
        niz_instrukcija = RucnaInicijalizacija(i)  # Inicijalizujem random GKV
        jedinka = Simulacija(niz_instrukcija, Blok)  # stvaram jedinku
        Niz_Jedinki.append(jedinka.Niz_Instrukcija)  # U Niz_Jedinki ubacujem jedinke
        Niz_Fitnessa.append(FitU(jedinka.Trci()))


    for evolucija in range(0, Generacija):
        Niz_Jedinki, Niz_Fitnessa = Sort(Niz_Fitnessa, Niz_Jedinki)

        print(str(evolucija) + "\t" + str(Niz_Fitnessa[0]))

        Najbolji_Niz = Niz_Jedinki[:NajboljiBr]  # Selekcija 40% Najboljih poopulacija
        CrossOver_Niz = Niz_Jedinki[NajboljiBr:(Generacija - OstaliBr)]  # Koriscenje odbacenih populacija za CrossOver
        Ostalo = Niz_Jedinki[(br_Jedinki - OstaliBr):]  # Ostatak
        Niz_Jedinki = []
        Niz_Fitnessa = []

        for i in range(0, CrossPop, 2):
            CrossOver_Niz[i], CrossOver_Niz[i + 1] = RandomCrossOver(CrossOver_Niz[i], CrossOver_Niz[i + 1])
        for i in range(0, OstaliBr):
            Ostalo[i] = RandomZaPopulaciju()  # Za ostatak Niza ubaciti random G, K, V
            # print(Ostalo[i])
        Niz_Jedinki = Najbolji_Niz + CrossOver_Niz + Ostalo  # Spajanje GKV
        for i in range(0, br_Jedinki):
            Deca = Simulacija(Niz_Jedinki[i], Blok)  # Pravljenje dece
            Niz_Fitnessa.append(FitU(Deca.Trci()))
        # pygame.display.flip()
        for i in range(0, br_Jedinki):
            Niz_Jedinki[i] = Mutacija(Niz_Jedinki[i])

        from multiprocessing import Pool
        from itertools import repeat
        with Pool(20) as pool:
            Niz_Fitnessa = list(pool.map(oceni, zip(Niz_Jedinki, repeat(Blok))))


def oceni(par):
    jedinka, Blok = par
    Deca = Simulacija(jedinka, Blok)  # Pravljenje dece
    return FitU(Deca.Trci())


if __name__ == '__main__':
    main()