"""Reforzamiento 03"""

"""Ejercicio 05"""

"""5. Crear una lista (entre floats y bools, 6 elementos mínimo) donde imprimas el penúltimo y antepenúltimo valor (por índice). 
Reconocer cada uno de los tipos de datos en esta lista creada y mostrar los resultados en consola"""

#Lista
lista = [3.5, 20.54, True, 3.9, 2.1, False, 9.3, True]

#Imprimir penultimo y antepenultimo
penultimo = lista[-2]
antepenultimo = lista[-3]
print("El penúltimo dato es: {}".format(penultimo))
print("El antepenultimo dato es: {}".format(antepenultimo))

print(" ")
#Tipos de datos
print("El dato {}, es de tipo {}".format(lista[0], type(lista[0])))
print("El dato {}, es de tipo {}".format(lista[1], type(lista[1])))
print("El dato {}, es de tipo {}".format(lista[2], type(lista[2])))
print("El dato {}, es de tipo {}".format(lista[3], type(lista[3])))
print("El dato {}, es de tipo {}".format(lista[4], type(lista[4])))
print("El dato {}, es de tipo {}".format(lista[5], type(lista[5])))
print("El dato {}, es de tipo {}".format(lista[6], type(lista[6])))
print("El dato {}, es de tipo {}".format(lista[7], type(lista[7])))

