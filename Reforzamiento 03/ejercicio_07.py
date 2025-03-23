"""Reforzamiento 03"""

"""Ejercicio 07"""

"""7. Crea una lista vacía, luego ingresa sus valores (10 valores numéricos) y
 finalmente muestra la suma y la media de los números ingresado insertados en la terminal"""

#Lista vacia
lista_01 = [ ]

#Agregar valores
lista_01.append(10)
lista_01.append(5.2)
lista_01.append(8.2)
lista_01.append(6.2)
lista_01.append(12)
lista_01.append(15.3)
lista_01.append(21.7)
lista_01.append(3.6)
lista_01.append(5.4)
lista_01.append(11.9)

#Suma y la media
suma_elem = sum(lista_01)
media_elem = sum(lista_01)/len(lista_01)
print("La suma de elementos es: {}".format(suma_elem))
print("La media de elementos es: {}".format(media_elem))

