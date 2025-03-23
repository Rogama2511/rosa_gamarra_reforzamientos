"""Reforzamiento 03"""

"""Ejercicio 01"""

"""1. Agregar 5 Objetos nuevos a tu lista (append) y quitar 2 elementos de esta lista por valor. 
Mostrar la lista final en la terminal. Obtén también la cantidad total ítems que tienes en tu lista 
ya creada para agregar este valor a tu lista y mostrar también el resultado final de cantidad total 
de elemento y la lista actualizada en consola.
"""

list_01 = ["México", "Ecuador", "Suiza"]

#Agregar elementos
list_01.append("Perú")
list_01.append("España")
list_01.append("Italia")
list_01.append("Brazil")
list_01.append("Argentina")

print(list_01)

#Quitar 2 elementos
list_01.remove("Brazil")
list_01.remove("México")
print("Lista 01: {}".format(list_01))

#Cantidad de elementos de la lista
cant_elementos = len(list_01)
list_01.append(cant_elementos)

print(" ")
print("Cantidad total de elementos: {}" .format(len(list_01)))
print("Lista actualizada: {}".format(list_01))



