from random import randint, seed
import matplotlib.pyplot as plt
import numpy as np

nro_elegido = 0  # int(input('Elija un numero de la ruleta (0-36):'))
# while nro_elegido < 0 or nro_elegido > 36:
#    nro_elegido = int(input('Elija un numero de la ruleta (0-36):'))

# Numero de iteraciones
iteraciones = 5
# Numero de tiradas
tiradas = 1000

fr = []
med = []
desv = []
var = []
valores = []
base = np.arange(37)

for i in range(iteraciones):
    count = 0
    fr.clear()
    med.clear()
    desv.clear()
    var.clear()
    valores.clear()
    seed(800+i)

    for t in range(tiradas):
        rand = randint(0, 36)
        valores.append(rand)
        if rand == nro_elegido:
            count += 1
        fr.append(count / (t + 1))
        med.append(np.mean(valores))
        desv.append(np.std(valores))
        var.append(np.var(valores))

    plt.subplot(2, 2, 1)
    plt.title('Frecuencia Relativa')
    plt.plot(fr)

    plt.subplot(2, 2, 2)
    plt.title('Media')
    plt.plot(med)

    plt.subplot(2, 2, 3)
    plt.title('Varianza')
    plt.plot(var)

    plt.subplot(2, 2, 4)
    plt.title('Desviacion Estandar')
    plt.plot(desv)

plt.subplot(2, 2, 1)
plt.plot([0, tiradas], [1 / len(base), 1 / len(base)], label="FR Esperada")
plt.legend(loc="upper right")
plt.ylabel('FR para el numero ' + str(nro_elegido))
plt.xlabel('n(numero de tiradas)')

plt.subplot(2, 2, 2)
plt.plot([0, tiradas], [np.mean(base), np.mean(base)], label="Media Esperada")
plt.legend(loc="upper right")
plt.ylabel('Valor Promedio')
plt.xlabel('n(numero de tiradas)')

plt.subplot(2, 2, 3)
plt.plot([0, tiradas], [np.var(base), np.var(base)], label="Varianza Esperada")
plt.legend(loc="upper right")
plt.ylabel('Valor de Varianza')
plt.xlabel('n(numero de tiradas)')

plt.subplot(2, 2, 4)
plt.plot([0, tiradas], [np.std(base), np.std(base)], label="VD Esperado")
plt.legend(loc="upper right")
plt.ylabel('Valor de Desvio')
plt.xlabel('n(numero de tiradas)')

plt.show()
