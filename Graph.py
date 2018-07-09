import matplotlib.pyplot as plt
def NacrtajGrafik(Niz):
    x = Niz

    plt.plot(x, label='Fitness')

    plt.xlabel('x label')
    plt.ylabel('y label')

    plt.title("Prkizaj najmanjeg Fitnessa tokom Evolucije")

    plt.legend()

    plt.show()