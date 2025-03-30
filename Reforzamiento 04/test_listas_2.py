"""Reforzamiento 04"""

"""Listas: Ejercicio 02"""

"""2. Crear un programa en Python donde tendrás una lista con 5 departamentos,
el programa te pedirá ingresar 2 departamentos el cual el segundo
departamento que ingreses sustituirá al primero de la lista."""

#Lista 5 departamento
lista_1  = ["Amazonas", "Lima", "Ancash", "Arequipa", "Cajamarca"]
print("Lista inicial: {}".format(lista_1))

#Ingresas dos departamentos
dept_1 = input("Ingresar un departamento:")
lista_1.append(dept_1)
dept_2 = input("Ingresar un departamento:")
lista_1[0] = dept_2


print("Lista final: {}".format(lista_1))

