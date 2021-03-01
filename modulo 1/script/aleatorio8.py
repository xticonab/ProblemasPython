# Problema 8
print('Problema 8')
import random

def numeros():
    lista = []
    for num in range(20):
        c = random.randint(0, 100)
        lista.append(c)
    return lista

def imprimir(lista):
    print(lista)

def orden(lista):
    return lista.sort()