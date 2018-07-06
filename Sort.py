
def Sort(Niz_Fitnessa, Niz_Jedinki):
    for i in range(len(Niz_Fitnessa) - 1):
        for j in range(i + 1, len(Niz_Fitnessa)):
            if Niz_Fitnessa[i] > Niz_Fitnessa[j]:           #Na osnovu Fitnessa se sortira lista jedinki
                temp = Niz_Fitnessa[i]
                prom = Niz_Jedinki[i]
                Niz_Fitnessa[i] = Niz_Fitnessa[j]
                Niz_Jedinki[i] = Niz_Jedinki[j]
                Niz_Fitnessa[j] = temp
                Niz_Jedinki[j] = prom
    return Niz_Jedinki, Niz_Fitnessa


