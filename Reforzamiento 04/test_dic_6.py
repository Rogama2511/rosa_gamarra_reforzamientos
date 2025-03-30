"""Reforzamiento 04"""

"""Diccionarios: Ejercicio 06"""

"""6. Ingresar por consola 4 números mediante consola, crear un diccionario
donde los ‘key’ serán los números indicados y los valores serán los cubos de
las estos keys. Mostrar finalmente este diccionario. """

#Diccionario
diccionario = { }

#Ingresar 4 numeros
for i in range(4):
    number = int(input(f"Ingresa el número {i+1}: "))
    diccionario[number] = number**3

#Mostrar el diccionario de cubos
print("El diccionario es: {}".format(diccionario))

