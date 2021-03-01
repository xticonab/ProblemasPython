# Problema 9
print('Problema 9')

import random

def numero():
    return int(input('Ingrese un numero entero: '))

def aleatorio():
    return random.randint(1, 100)

def adivinar():
    x = aleatorio()
    imprimir('Bienvenido al juego de adivina el numero')
    imprimir('A ver si eres capaz de adivininarlo')
    correcto = False

    while correcto == False:
        n = numero()
        if x == n:
            imprimir('Has ganado')
            correcto = True
        elif x < n:
            imprimir('El valor introducido es menor')
        else:
            imprimir('El valor introducido es mayor')

def imprimir(texto):
    print(texto)