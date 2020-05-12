import random as rn
import matplotlib.pyplot as plt

# la idea seria aplicar la martingala hasta quedarnos sin plata
# probamos apostando al rojo

# ruleta
min_n = 0
max_n = 36
numeros_rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 20, 21, 23, 25, 27, 29, 31, 32, 34, 36]
# numeros_negros = [2, 4, 6, 8, 10, 11, 13, 15, 17, 19, 22, 24, 26, 28, 30, 33, 35]  Esta de referencia nomas, no se usa

# Fibonacci  asdasdasd            consiste en que si perdes te moves para la derecha 1 punto, si ganas te moves dos para la izq
lista_fibonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

# finito
lista_numeros = []
lista_dinero = []

# infinito
lista_numeros2 = []
lista_dinero2 = []

# iniciales
dinero_inicial = 1000
apuesta_minima = 10


def getColor(numero):  # conviene crear esta funcion ? lo hago para que sea mas legible el codigo dentro de apuesta
    if numero in numeros_rojos:
        return "rojo"
    elif numero == 0:
        return "sin"
    else:
        return "negro"


def actualizaPuntero(p, tipo):  # 0 perdedor, 1 ganador
    if tipo == 0:
        return p + 1
    elif p - 2 < 0:
        p = 0
    else:
        p -= 2
    return p


def apuesta_dinero():
    dinero = dinero_inicial
    apuesta = apuesta_minima
    puntero_fib = 0
    while dinero >= 0 and puntero_fib <= 15:
        lista_dinero.append(dinero)
        if apuesta > lista_dinero[-1]:
            #print("no tiene tanto dinero, saldo final:", dinero)
            break
        lista_numeros.append(rn.randint(min_n, max_n))
        if getColor(lista_numeros[-1]) == "rojo":
            puntero_fib = actualizaPuntero(puntero_fib, 1)
            dinero += apuesta
        else:
            puntero_fib = actualizaPuntero(puntero_fib, 0)
            if getColor(lista_numeros[-1]) == "negro":
                dinero -= apuesta
            else:
                dinero -= apuesta / 2  # el cero solo te hace perder la mitad de lo que apostaste. ver paper
        apuesta = apuesta_minima * lista_fibonacci[puntero_fib]
    if puntero_fib >= 15:
        print("Ganaste")
    return lista_dinero


def apuesta_n_veces(n):
    dinero = dinero_inicial
    apuesta = apuesta_minima
    puntero_fib = 0
    for i in range (0, n):
        lista_dinero2.append(dinero)
        if puntero_fib >= 15:
            print("Ganaste", dinero)
            break
        lista_numeros2.append(rn.randint(min_n, max_n))
        if getColor(lista_numeros2[-1]) == "rojo":
            puntero_fib = actualizaPuntero(puntero_fib, 1)
            dinero += apuesta
        else:
            puntero_fib = actualizaPuntero(puntero_fib, 0)
            if getColor(lista_numeros2[-1]) == "negro":
                dinero -= apuesta
            else:
                dinero -= apuesta / 2  # el cero solo te hace perder la mitad de lo que apostaste. ver paper
        apuesta = apuesta_minima * lista_fibonacci[puntero_fib]
    return lista_dinero2


def plot_dinero(li):  # plotea la cantidad de plata que tenes en caja
    plt.subplot()
    plt.xlabel('Cantidad de tiradas')
    plt.ylabel('Caja')
    plt.title("Fibonacci")
    plt.plot(li, label="dinero")
    plt.plot([0, len(li)], [dinero_inicial, dinero_inicial])
    plt.legend()
    plt.show()


def main():
    veces = 1000
    plot_dinero(apuesta_dinero())
    plot_dinero(apuesta_n_veces(veces))

main()
