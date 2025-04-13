
"""
Para test_03
- Una función que genere 30 números enteros aleatorios entre 0 y 100,
y muestre en pantalla esta lista de números aleatorios
- Otra función que ordene los valores de una lista y volver a mostrarla en pantalla
- Otra función que me indicará cuál es el mayor de todos estos números de la lista
"""
import random

def lista_num():
    numero = random.randint(0,100)
    lista = []
    for numero in range(30):
        while numero not in lista and len(lista) < 30:
            lista.append(numero)
            numero = random.randint(0,100)
    print("Lista: ")
    print(lista)
    return lista

def ordenar_lista(lista):
    lista.sort()
    print("Lista ordenada:")
    print(lista)
    return lista

def mayor_num(lista):
    mayor = max(lista)
    print("El número mayor es: {}".format(mayor))
    return mayor
