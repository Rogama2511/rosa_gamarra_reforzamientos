"""Reforzamiento 04"""

"""Diccionarios: Ejercicio 05"""

"""5. Ingresar el nombre de tu carrera dentro de los valores que tienes en tu
diccionario.
- Mostrar en consola los valores de tu carrera y nombre agregándolos a
una variable c/u """

#Definir  diccionario
dicc_1 = {"nombre": "Rosa", "edad": 20, "salario": 3000}

#Ingresar carrera
dicc_1["carrera"] = "Física"
print("Lista actualizada: {}".format(dicc_1))

#Mostrar valores carrera y nombre
carrera = dicc_1["carrera"]
nombre = dicc_1["nombre"]

print("El valor carrera es {}".format(carrera))
print("El valor nombre es {}".format(nombre))

