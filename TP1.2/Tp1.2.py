import random as rn
#la idea seria aplicar la martingala hasta quedarnos sin plata
#probamos apostando al rojo

apuesta_minima = 10
min_n = 0
max_n = 36
numeros_rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 20, 21, 23, 25, 27, 29, 31, 32, 34, 36]
numeros_negros = [2, 4, 6, 8, 10, 11, 13, 15, 17, 19, 22, 24, 26, 28, 30, 33, 35]
numeros_cero = 0
lista = []

for i in range(0, 30):
        dinero = 1000
        apuesta = apuesta_minima
        count = 0
        while dinero >= 0:
            if apuesta > dinero:
                print("no tiene tanto dinero, saldo final:", dinero, "cantidad de tiradas:", count)
                break
            count+=1
            lista.append(rn.randint(min_n, max_n))
            if lista[-1] in numeros_rojos:
                dinero += apuesta
                apuesta = apuesta_minima
            else:
                dinero -= apuesta
                apuesta *= 2

            #print(lista[-1], dinero)




