"""
Para test_02
- Una función que realizará la carga de un valor entero y que verifique
que solamente tiene que ser numérico
- Una función que mostrará por pantalla la raíz cuadrada de dicho valor
- Y otra función el valor elevado al cuadrado y al cubo de dicho número,
puedes devolver un diccionario
- Utilizar el módulo math de python
"""
import math
from math import sqrt

# Ingresar número
def ingresar_num():
    try:
        numero = int(input("Ingresa un numero: "))
        return numero
    except TypeError:
        print("El numero que ingrese debe ser un entero")

# Raiz cuadrada
def raiz(numero):
    try:
        return math.sqrt(numero)
    except ValueError:
        print("La raiz de un número negativo es un complejo")

# Evelar al cuadrado y cubo
def elevar(numero):
    cuadrado = numero ** 2
    cubo = numero ** 3
    return cuadrado, cubo

