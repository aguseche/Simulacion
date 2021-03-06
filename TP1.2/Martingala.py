import random as rn
import matplotlib.pyplot as plt

# la idea seria aplicar la martingala hasta quedarnos sin plata
# probamos apostando al rojo

# ruleta
min_n = 0
max_n = 36
numeros_rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 20, 21, 23, 25, 27, 29, 31, 32, 34, 36]
# numeros_negros = [2, 4, 6, 8, 10, 11, 13, 15, 17, 19, 22, 24, 26, 28, 30, 33, 35]  Esta de referencia nomas, no se usa

# finito
lista_numeros = []
lista_dinero = []

# infinito
lista_numeros2 = []
lista_dinero2 = []

# iniciales
dinero_inicial = 1000
apuesta_minima = 10


def getColor(numero):
    if numero in numeros_rojos:
        return "rojo"
    elif numero == 0:
        return "sin"
    else:
        return "negro"


def apuesta_dinero():
    dinero = dinero_inicial
    apuesta = apuesta_minima
    count = 0
    while dinero >= 0:
        lista_dinero.append(dinero)
        if apuesta > dinero:
            #print("no tiene tanto dinero, saldo final:", dinero, "cantidad de tiradas:", count)
            break
        lista_numeros.append(rn.randint(min_n, max_n))
        if getColor(lista_numeros[-1]) == "rojo":
            dinero += apuesta
            apuesta = apuesta_minima  # resetea valor en caso de ganar
        else:
            if getColor(lista_numeros[-1]) == "negro":
                dinero -= apuesta
            else:  # el cero solo te hace perder la mitad de lo que apostaste. ver paper
                dinero -= apuesta / 2
            apuesta *= 2

        count += 1
    return lista_dinero


def apuesta_n_veces(n):
    dinero = dinero_inicial
    apuesta = apuesta_minima
    for i in range(0, n):
        lista_dinero2.append(dinero)
        lista_numeros2.append(rn.randint(min_n, max_n))
        if getColor(lista_numeros2[-1]) == "rojo":
            dinero += apuesta
            apuesta = apuesta_minima  # resetea valor en caso de ganar
        else:
            if getColor(lista_numeros2[-1]) == "negro":
                dinero -= apuesta
            else:
                dinero -= apuesta / 2
            apuesta *= 2
    return lista_dinero2


def plot_dinero(li):  # plotea la cantidad de plata que tenes en caja
    plt.subplot()
    plt.xlabel('Cantidad de tiradas')
    plt.ylabel('Caja')
    plt.title("La Martingala")
    plt.plot(li, label="dinero")
    plt.plot([0, len(li)], [dinero_inicial, dinero_inicial])
    plt.legend()
    plt.show()


'''
def calcula_fr(): #calcular fr para pasar al plot
    lista_x = []
    contador = 0
    for i in range (0, lista_dinero):
        if lista_dinero[i] < lista_dinero[i+1]: #ganas
            contador += 1
        elif lista_dinero[i] > lista_dinero[i+1]: #perdes
            pass
        else:
            pass
'''


def plot_fr():  # plotea la frecuencia relativa de tener una apuesta favorable segun n
    pass


def main():
    # veces = int(input("Ingrese cuantas veces quiere repetir las tiradas: "))
    veces = 1000
    plot_dinero(apuesta_dinero())
    plot_dinero(apuesta_n_veces(veces))


main()
