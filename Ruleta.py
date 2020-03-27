#Como ejercicio tenemos que hacer una ruleta y hacer las graficas de ...
#import random as ran
import numpy as np
import matplotlib as matp


def mensaje():
    print ("Bienvenido a la ruleta!!")


def ruleta():
    n = np.randint(0, 36)
    return n


def opciones():
    numeros = []
    op = "S"
    while op == "S":
        num = ruleta()
        numeros.append(num)
        print(num)
        op = input("Ingrese S para conseguir otro numero: ").upper()
    print("Finalizado.")
    return numeros

def Calculo(lis):
    pass


def main():
    mensaje()
    lista = opciones()
    print(lista)


main()
