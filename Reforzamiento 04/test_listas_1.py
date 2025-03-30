"""Reforzamiento 04"""

"""Listas: Ejercicio 01"""

"""1. Escribir un programa donde ingresarás el tamaño de la lista mediante
consola, este tamaño servirá para ingresar una cantidad X de nombres de
alumnos. Ingresarás los nombres mediante consola también.
Se quiere mostrar finalmente el tamaño de la lista y todos los nombres de
la lista que fueron ingresados."""

#Tamaño de lista
num_nombres = int(input("Ingresar tamaño de la lista: "))

#Definir lista
list_nombres = []

#Ingresar nombres usando el tamaño de la lista
for i in range(num_nombres):
    nombres = input(f"Ingresar nombre {i + 1}: ")
    list_nombres.append(nombres)

#Lista completa de nombres
print(list_nombres)