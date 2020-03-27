#Como ejercicio tenemos que hacer una ruleta y hacer las graficas de ...
import random as ran

def mensaje():
    print ("Bienvenido a la ruleta!!")


def ruleta():
    n = ran.randint(0, 36)
    return n

def main():
    mensaje()
    op = "S"
    while op == "S":
        num = ruleta()
        print(num)
        op = input("Ingrese S para conseguir otro numero: ").upper()
    print("Finalizado.")


main()
