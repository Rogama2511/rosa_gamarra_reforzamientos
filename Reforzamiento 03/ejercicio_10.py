"""Reforzamiento 03"""

"""Ejercicio 10"""

"""10. Tienes una lista con 7 diferentes nombres de BD relacionales. 
De la cual 3 BDs estarán repetidas adrede (en posiciones no consecutivas), 
sacar la base de datos repetidas uno por valor y le otro por índice.
Finalmente mostrar la lista actualizada en consola. """

#Lista BD
lista_bd = ["MySQL", "PostgreSQL", "Oracle", "SQL Server", "MySQL", "SQLite", "MySQL"]
print("Lista BD: {}".format(lista_bd))

#Eliminar una base de datos repetida
lista_bd.remove("MySQL")
del lista_bd[3]

#Lista actualizada
print("Lista actualizada: {}".format(lista_bd))