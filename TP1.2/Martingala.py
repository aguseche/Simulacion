import random as rn
from typing import List, Any

import matplotlib.pyplot as plt

# la idea seria aplicar la martingala hasta quedarnos sin plata
# probamos apostando al rojo

apuesta_minima = 10
min_n = 0
max_n = 36
numeros_rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 20, 21, 23, 25, 27, 29, 31, 32, 34, 36]
numeros_negros = [2, 4, 6, 8, 10, 11, 13, 15, 17, 19, 22, 24, 26, 28, 30, 33, 35]
numeros_cero = 0
lista_numeros = []
lista_plata = []
dinero_inicial = 1000


def apuesta():
    dinero = dinero_inicial
    apuesta = apuesta_minima
    count = 0
    while dinero >= 0:
        lista_plata.append(dinero)
        if apuesta > dinero:
            print("no tiene tanto dinero, saldo final:", dinero, "cantidad de tiradas:", count)
            break
        count += 1
        lista_numeros.append(rn.randint(min_n, max_n))
        if lista_numeros[-1] in numeros_rojos:
            dinero += apuesta
            apuesta = apuesta_minima  # resetea valor
        else:
            dinero -= apuesta
            apuesta *= 2
    return lista_plata


def plot_dinero(li):  # plotea la cantidad de plata que tenes en caja
    plt.subplot(2, 1, 1)
    plt.xlabel('Cantidad de tiradas')
    plt.ylabel('Caja')
    plt.title("La Martingala")
    plt.plot(li, label="dinero")
    plt.plot([0, len(li)], [dinero_inicial, dinero_inicial])
    plt.legend()
    plt.show()


def plot_fr():  # plotea la frecuencia relativa de tener una apuesta favorable segun n
    pass


def main():
    plot_dinero(apuesta())


main()
