"""Reforzamiento 04"""

"""Diccionarios: Ejercicio 04"""

"""4. Crear un diccionario con 6 departamentos en el país.
- Borrar cualquier departamento, usando la palabra reservada del.
- Actualizar el penúltimo departamento por otro.
- Comprobar que no existe este departamento borrado dentro del
diccionario."""

#Crear diccionario
departamento = {"dep1":"Lima", "dep2": "Arequipa","dep3": "Cusco",
                "dep4": "Piura", "dep5": "Trujillo", "dep6": "Loreto"}

#Borrar cualquier departamento
del departamento["dep2"]

#Actualizar penultimo departamento
list= list(departamento.keys())
del_dep = list[-2]

departamento[del_dep] = "Huanuco"
print("Lista de departamentos: {}".format(departamento))

#Comprobar el departamento borrado
print("¿Existe el departamento 'Arequipa' en el diccionario?: {}".format("dep2" in departamento))
