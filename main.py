import copy
import pygame
from Kretanje import *
from Unos import  *
import numpy
import math
import random
from Inizijalizacija import*
from Sort import Sort
from KlasaSimulacija import *
from CrossOver import *
from Mutacija import *
# pygame.init()
#
# clock = pygame.time.Clock()     # load clock
#
#
# pygame.time.set_timer(pygame.USEREVENT,10)
#
# button = pygame.Rect(160, 450, 140, 32)
#
# APPLICATION_x_size = 500
# APPLICATION_y_size = 800
#
# # a color can be: (0 to 255, 0 to 255, 0 to 255)
# My_light_blue_color = (190, 190, 255)
# My_light_red_color = (182, 0, 0)
# FONT = pygame.font.Font(None, 32)
#
# screen = pygame.display.set_mode((APPLICATION_x_size, APPLICATION_y_size))
# pygame.display.set_caption('Simulacija')
# pygame.mouse.set_visible(True)
# black_square_that_is_the_size_of_the_screen = pygame.Surface(screen.get_size())
# black_square_that_is_the_size_of_the_screen.fill((0, 0, 0))
# screen.blit(black_square_that_is_the_size_of_the_screen, (0, 0))
# pygame.display.flip()

def main():
    done = False
    brzinaStaraX = 0
    brzinaStaraY = 0
    start_x = 170  # x kordinata pocetnog bloka
    start_y = 760  # y kordinata pocetnog bloka
    x_size = 50  # duzina bloka
    y_size = 30  # sirina bloka
    x = start_x
    y = start_y
    playerX = 194
    playerY = 775
    # pygame.draw.rect(screen, My_light_blue_color, (x, y, x_size, y_size))  # prvi blok
    # player = pygame.Rect((playerX, playerY, 4, 4))  # pocetna pozicija igraca
    # pygame.draw.rect(screen, My_light_red_color, player)
    # pygame.display.update()
    ix = 0
    Skretanje = [0]*50
    Blok = [0]*50
    # pygame.mouse.set_visible(False)
    #     while not done:

        # generisanje random mape
    while ix < 24:
        q = random.randint(0, 9)  # bira da li ce ici levo ili desno(0 - levo, 1 - desno
        Skretanje[ix] = q
        if q == 0:
            y = y - 30
            # pygame.draw.rect(screen, My_light_blue_color, (x, y, x_size, y_size))
        elif q == 1:
            x = x + 20
            y = y - 30
            # pygame.draw.rect(screen, My_light_blue_color, (x, y, x_size, y_size))
        elif q == 2:
            x = x - 20
            y = y - 30
            # pygame.draw.rect(screen, My_light_blue_color, (x, y, x_size, y_size))
        elif q == 3:
            x = x - 10
            y = y - 30
            # pygame.draw.rect(screen, My_light_blue_color, (x, y, x_size, y_size))
        elif q == 4:
            x = x + 10
            y = y - 30
            # pygame.draw.rect(screen, My_light_blue_color, (x, y, x_size, y_size))
        elif q == 5:
            x = x - 5
            y = y - 30
            # pygame.draw.rect(screen, My_light_blue_color, (x, y, x_size, y_size))
        elif q == 6:
            x = x + 5
            y = y - 30
            # pygame.draw.rect(screen, My_light_blue_color, (x, y, x_size, y_size))
        elif q == 7:
            x = x - 15
            y = y - 30
            # pygame.draw.rect(screen, My_light_blue_color, (x, y, x_size, y_size))
        elif q == 8:
            x = x + 15
            y = y - 30
                # pygame.draw.rect(screen, My_light_blue_color, (x, y, x_size, y_size))
        Blok[ix] = numpy.array([x, y])
        ix += 1
    Niz_Populacija = []
    Niz_Jedinki= []
    Niz_Fitnessa = []
        # pygame.display.flip()
    f = open("podaci.txt","w")
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         # print("Gas - Kocnica - Volan \t x0 - x - Brzina - Ubrzanje \n")
        #         done = True
                # stvaram 1000 populacija jedinki
    generacija = open("PrvaGeneracija.txt", "w")
    for i in range(0, 10000):
        niz_instrukcija = Inizijalizacija(Skretanje)  # Inicijalizujem random GKV
        jedinka = Simulacija(niz_instrukcija, Blok)  # stvaram jedinku
        Niz_Jedinki.append(jedinka.Niz_Instrukcija)  # U Niz_Jedinki ubacujem jedinke
        Niz_Fitnessa.append(FitU(jedinka.Trci()))  # U Niz Fitnessa ubacujem Fitness od jedinke
        generacija.write(str(niz_instrukcija))

    # Evolucija
    for evolucija in range(0, 10000):
        Niz_Jedinki, Niz_Fitnessa = Sort(Niz_Fitnessa, Niz_Jedinki)  # Na kraju sortiram Niz_Jedinki na osnovu Fitnesa
        f.write(str(Niz_Fitnessa[0]) + "\n")
        print(str(evolucija) + "\t" + str(Niz_Fitnessa[0]))
        Najbolji_Niz = Niz_Jedinki[:4000]  # Selekcija 40% Najboljih poopulacija
        Odbaceni_Niz = Niz_Jedinki[4000:7000]  # Koriscenje odbacenih populacija za CrossOver
        Ostalo = Niz_Jedinki[7000:]  # Ostatak
        Niz_Jedinki = []
        Niz_Fitnessa = []
        for i in range(0, 3000, 2):
            Odbaceni_Niz[i], Odbaceni_Niz[i + 1] = TwoPoint(Odbaceni_Niz[i], Odbaceni_Niz[i + 1])
            # print(Odbaceni_Niz[i])                                #Cuveni One Point crossover
        for i in range(0, 3000):
            Ostalo[i] = RandomZaPopulaciju()  # Za ostatak Niza ubaciti random G, K, V
            # print(Ostalo[i])
        Niz_Jedinki = Najbolji_Niz + Odbaceni_Niz + Ostalo  # Spajanje GKV
        for i in range(0, 10000):
            Deca = Simulacija(Niz_Jedinki[i], Blok)  # Pravljenje dece
            Niz_Fitnessa.append(FitU(Deca.Trci()))
        # pygame.display.flip()
        for i in range(0, 10000):
            Niz_Jedinki[i] = Mutacija(Niz_Jedinki[i])


        from multiprocessing import Pool
        from itertools import  repeat
        with Pool(20) as pool:
            Niz_Fitnessa = list(pool.map(oceni, zip(Niz_Jedinki, repeat(Blok))))

def oceni(par):
    jedinka, Blok = par
    Deca = Simulacija(jedinka, Blok)  # Pravljenje dece
    return FitU(Deca.Trci())
if __name__ == '__main__':
    main()
    # pygame.quit()