"""Reforzamiento 03"""

"""Ejercicio 11"""

"""11. Ingresar compañías relacionadas con al mundo de TI, 
copia los elementos de la lista en otra lista pero estarán orden inverso, 
y muestra sus elementos por la terminal y la lista original también."""

#Lista compañias
lista_companias = ["Microsoft", "Apple", "Google", "Amazon", "Oracle"]

#Copiar elementos
lista_companias02 = lista_companias.copy()
lista_companias02.reverse()

print("Lista inversa:{}".format(lista_companias02))
print("Lista original: {}".format(lista_companias))
