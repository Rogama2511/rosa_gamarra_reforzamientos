"""Reforzamiento 03"""

"""Ejercicio 03"""

"""3. Crea una siguiente lista vacía y agregue ítems a partir de variables 
(los cuales tendrán los siguientes tipos de datos: 3 floats, 3 ints y 3 strings) (append).
Sumar las dos listas creadas anteriormente y mostrar el resultado en consola."""

#Lista vacia
list_01 = []

list_02 = [6.5, 12.1, 3, -1, "Biologia"]

#Variables
float1 = 3.02
float2 = 43.2
float3 = 5.7
int1 = 25
int2 = -13
int3 = 5
str1 = "Física"
str2 = "Matemática"
str3 = "Química"

#Agregar a la lista
list_01.append(float1)
list_01.append(float2)
list_01.append(float3)
list_01.append(int1)
list_01.append(int2)
list_01.append(int3)
list_01.append(str1)
list_01.append(str2)
list_01.append(str3)

#Listas
print("Lista 01: {}".format(list_01))
print("Lista 02: {}".format(list_02))

#Suma de las listas
lista_combinada = list_01 + list_02
print("Lista Combinada: {}".format(lista_combinada))