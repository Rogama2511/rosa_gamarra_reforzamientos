"""Reforzamiento 04"""

"""Diccionarios: Ejercicio 03"""

"""3. Convertir tu diccionario a una lista y mostrar en consola el tipo de datos
final que tiene."""


#Definir  diccionario
dicc_1 = {"nombre": "Rosa", "edad": 20, "salario": 3000}

#Convertir dicc a lista
lista = list(dicc_1.values())
print("Lista de datos: {}".format(lista))

#Tipo de datos
print("Tipo de dato final de la lista: {}".format(type(lista)))
print("Tipos de datos en la lista:", [type(item) for item in lista])

