import random as rn

dinero = 1000
apuesta_minima = 10
min_n = 0
max_n = 36


def tirada():
    return rn.randint(min_n, max_n)


def main():
    color = (input("Ingrese color: (r o n)"))
    numero = tirada()
    print(numero)
    if numero % 2 == 1 and color == "r":
        print("Bien")
    elif numero % 2 == 1 and color == "n":
        print("mal")
    else:
        print("Bien")


main()
