#Sort Jedinki da bi se izuvkle jedinke sa najboljim Fitnessom
#Niz_Objekata - je u stvari Niz Fitnessa
def Sort(Niz_Objekata, Niz_Jedinki):
    for passnum in range(len(Niz_Objekata) - 1):
        for i in range(passnum + 1, len(Niz_Objekata)):
            if (Niz_Objekata[passnum] > Niz_Objekata[i]):           #Na osnovu Fitnessa se sortira lista jedinki
                temp = Niz_Objekata[passnum]
                prom = Niz_Jedinki[passnum]
                Niz_Objekata[passnum] = Niz_Objekata[i]
                Niz_Jedinki[passnum] = Niz_Jedinki[i]
                Niz_Objekata[i] = temp
                Niz_Jedinki[i] = prom
    return Niz_Jedinki, Niz_Objekata

