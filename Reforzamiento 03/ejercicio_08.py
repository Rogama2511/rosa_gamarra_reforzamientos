"""Reforzamiento 03"""

"""Ejercicio 08"""

"""8. Escribir un programa donde ingresará 8 nombres de países. Se quiere hacer un clon de la lista, 
esta copia se le eliminará el primer y penúltimo valor, mostrar finalmente el tamaño de la lista modificada, 
la lista original y todos sus elementos de la lista modificada. """

#Lista
paises = ["México", "Brasil", "Argentina", "Colombia", "Perú", "Chile", "Ecuador", "Uruguay"]

#Clon de la lista
paises_clon = paises.copy()

#Eliminar el primer y penúltimo valor
del paises_clon[0]
del paises_clon[-2]

print("Tamaño de la lista modificada: ".format(len(paises_clon)))
print("Lista original: {}".format(paises))
print("Lista modificada: {}".format(paises_clon))

