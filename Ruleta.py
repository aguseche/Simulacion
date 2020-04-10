# Como ejercicio tenemos que hacer una ruleta y hacer las graficas
# 1- fr/n frecuencia relativa #cantidad de veces que SALIO el numero / cantidad total de muestras
# 2- vp/n valor promedio de las tiradas
# 3- vd/n valor del desvio       np.std(datos, 0) # Desviación típica de cada columna
# 4- vv/n valor de la varianza
import numpy as np
import matplotlib.pyplot as plt
import random as rn
import matplotlib.ticker as tick
import statistics as st


n_muestras = 1000
min_n = 0
max_n = 36

data = []
media = []
media_media = []
varianza = []
varianza_media = []
desviacion = []


def cambiar_y(x, pos):
    return x / len(data)


def plot_frAbs(d):  # graficar histograma de frecuencias absolutas
    fig, ax = plt.subplots()
    ax.hist(d, bins=max_n + 1)
    fig.tight_layout()
    ax.set_xlabel('Numeros de la ruleta')
    ax.set_ylabel('Cantidad')
    plt.title("Histograma de frecuencia absoluta")
    plt.show()


def plot_frRel(d):  # graficar histograma de frecuencias relativas
    fig, ax = plt.subplots()
    ax.hist(d, bins=max_n + 1)
    ax.yaxis.set_major_formatter(tick.FuncFormatter(cambiar_y))  # para cambiar los valores mostrados en y
    fig.tight_layout()
    ax.set_xlabel('Numeros de la ruleta')
    ax.set_ylabel('Cantidad / 100')
    plt.title("Histograma de frecuencia relativa")
    plt.show()


def plot_media(m):  # graficar histograma de media
    fig, ax = plt.subplots()
    plt.plot(list(range(len(m))), m, color='k')
    ax.set_xlabel('Cantidad de tiradas')
    ax.set_ylabel('Media')
    plt.title("Histograma de media")
    plt.show()


def plot_media_media(mm):  # graficar histograma de media de la media
    fig, ax = plt.subplots()
    plt.plot(list(range(len(mm))), mm, color='k')
    ax.set_xlabel('Cantidad de tiradas')
    ax.set_ylabel('Media de la media')
    plt.title("Histograma de media de la media")
    plt.show()


def plot_mymm(m, mm):   #graficar conjuntamente media y media de media
    fig, ax = plt.subplots()
    plt.plot(list(range(len(m))), m, color='k')
    plt.plot(list(range(len(mm))), mm, color='white')
    ax.xlabel('Cantidad de tiradas')
    ax.ylabel('Medias')
    plt.title("Histograma de media de la media")
    plt.show()

def plot_varianza(v):
    fig, ax = plt.subplots()
    plt.plot(list(range(len(v))), v, color='k')
    ax.set_xlabel('Cantidad de tiradas')
    ax.set_ylabel('varianza')
    plt.title("Histograma de varianza")
    plt.show()



def plot_varianza_media(vm):
    fig, ax = plt.subplots()
    plt.plot(list(range(len(vm))), vm, color='k')
    ax.set_xlabel('Cantidad de tiradas')
    ax.set_ylabel('varianza de la media')
    plt.title("Histograma de varianza de la media")
    plt.show()

def plot_desviacion(des):
    plt.subplot(2, 2, 1)
    plt.title('desviacion')
    plt.xlabel('cantidad de tiradas')
    plt.ylabel('desviacion')
    plt.plot(des)
    plt.show()

def plot(d, m, mm, v, vm, des):
    #plot_frAbs(d)
    #plot_frRel(d)
    #plot_media(m)
    #plot_media_media(mm)
    #plot_mymm(m, mm)
    #plot_varianza(v)
    #plot_varianza_media(vm)
    plot_desviacion(des)


def mostrar_datos(d):
    for i in range(min_n, max_n + 1):
        print(str(i) + ": " + str(d.count(i)))


def main():
    for i in range(n_muestras):
        data.append(rn.randint(min_n, max_n))
        media.append(np.mean(data))
        media_media.append(np.mean(media))
        desviacion.append(np.std(data))
        if i >=2:
            varianza.append(st.variance(data))
            varianza_media.append(st.variance(media))

    plot(data, media, media_media, varianza, varianza_media, desviacion)
    mostrar_datos(data)


main()
