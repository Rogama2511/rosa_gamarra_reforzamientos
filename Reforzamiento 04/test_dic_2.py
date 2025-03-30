"""Reforzamiento 04"""

"""Diccionarios: Ejercicio 02"""

"""2. Agrega un nuevo key llamado “dni” con su respectivo valor y luego mostrar
el valor del salario y DNI en consola. También elimina el key edad de tu
diccionario, incluyendo su valor. Mostrar finalmente el diccionario
actualizado."""

#Definir  diccionario
dicc_1 = {"nombre": "Rosa", "edad": 20, "salario": 3000}

#Agregar DNI
dicc_1["DNI"] = 7819324
print("Datos iniciales: {}".format(list(dicc_1.values())))

print("Valor del salario: {}".format(dicc_1["salario"]))
print("Valor del DNI: {}".format(dicc_1["DNI"]))

#Eliminar la edad
del dicc_1["edad"]

print("Diccionario actualizado: {}".format(dicc_1))

