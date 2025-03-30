"""Reforzamiento 04"""

"""Listas: Ejercicio 04"""

"""4. Ingresar por consola el tamaño de una lista, luego empezarás a ingresar los
datos mediante consola también (5 compañías relacionadas con al mundo de
TI) y harás una copia donde adrede agregarás nombres que estarán
repetidos (mediante consola) para que finalmente muestres otra lista donde
solo se mostrará los nombres no repetidos y también la lista inicial."""

#Tamaño de lista
tam_lista = int(input("Ingresar tamaño de la lista: "))

list_TI = []

#Ingresar compañias TI
for i in range(tam_lista):
    camp_TI = input(f"Ingresar compañia {i+1}: ")
    list_TI.append(camp_TI)

#Hacer copia y agregar nombres repetidos
list2_TI = list_TI.copy()

num_TI = int(input(f"Ingresar número de compañias a ingresar:"))
for i in range(num_TI):
    new_comp = input("Ingresar nuevas compañias:")
    list2_TI.append(new_comp)

#Imprimir lista de valores unicos y lista inicial
print("Lista sin valores repetidos: {}".format(set(list2_TI)))
print("Lista inicial: {}".format(list_TI))




