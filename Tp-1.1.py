#Como ejercicio tenemos que hacer una ruleta y hacer las graficas
#1- fr/n frecuencia relativa #cantidad de veces que SALIO el numero / cantidad total de muestras
#2- vp/n valor promedio de las tiradas
#3- vd/n valor del desvio       np.std(datos, 0) # Desviación típica de cada columna
#4- vv/n valor de la varianza
import numpy as np
import pandas as pd

def mensaje():
    print ("Bienvenido a la ruleta!!")


def ruleta(n):
    return np.random.randint(0, 36, n)


def main():
    mensaje()
    d = ruleta(int(input("Ingrese la cantidad de muestras que desea: ")))
    print(d)


main()
