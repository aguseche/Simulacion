# Como ejercicio tenemos que hacer una ruleta y hacer las graficas
# 1- fr/n frecuencia relativa #cantidad de veces que SALIO el numero / cantidad total de muestras
# 2- vp/n valor promedio de las tiradas
# 3- vd/n valor del desvio       np.std(datos, 0) # Desviación típica de cada columna
# 4- vv/n valor de la varianza
import numpy as np
import matplotlib.pyplot as plt
import random as rn
import matplotlib.ticker as tick


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


def plot(d, m, mm, v, vm):
    # graficar histograma de frecuencias absolutas

    fig, ax = plt.subplots()
    ax.hist(d, bins=max_n + 1)
    fig.tight_layout()
    ax.set_xlabel('Numeros de la ruleta')
    ax.set_ylabel('Cantidad')
    plt.title("Histograma de frecuencia absoluta")
    plt.show()

    # graficar histograma de frecuencias relativas
    fig, ax = plt.subplots()
    ax.hist(d, bins=max_n + 1)
    ax.yaxis.set_major_formatter(tick.FuncFormatter(cambiar_y))  # para cambiar los valores mostrados en y
    fig.tight_layout()
    ax.set_xlabel('Numeros de la ruleta')
    ax.set_ylabel('Cantidad / 100')
    plt.title("Histograma de frecuencia absoluta")
    plt.show()


def plot_2(m, mm):
    # graficar histograma de media
    plt.subplots(2, 2, 1)
    plt.title('Media')
    plt.plot(m)

    # graficar histograma de media de media
    plt.subplots(2, 2, 2)
    plt.title('Media')
    plt.plot(mm)


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
            varianza.append(np.var(data))
            varianza_media.append(np.var(media))

    #plot(data, media, media_media, varianza, varianza_media, desviacion)
    plot_2(media, media_media)
    mostrar_datos(data)


main()
