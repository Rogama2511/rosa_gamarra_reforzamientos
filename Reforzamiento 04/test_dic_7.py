"""Reforzamiento 04"""

"""Diccionarios: Ejercicio 07"""

"""7. Realizar un programa donde se ingresarán por consola los nombres de los
alumnos (indicar previamente la cantidad de alumnos a ingresar) de un curso
y las notas de c/u. Guardarás la información en un diccionario donde las claves
serán los nombres de c/u de estos alumnos y sus valores serán las notas de
esto alumnos.
Finalmente mostrarás los alumnos con sus notas en un mensaje similar a
“Pedro tiene la nota de 15” y también la media de todas las notas."""

#Número de alumnos
num_alum = int(input("Ingrese la cantidad de alumnos: "))

#Diccionario de datos
dicc_notas = { }

#Ingresar nombres de alumnos
for i in range(num_alum):
    nombre = input(f"Ingrese nombre del alumno {i+1}: ")
    nota = float(input(f"Ingrese nota del alumno {i+1}: "))
    dicc_notas[nombre] = nota

#Mostrar diccionario
print("El diccionario de alumnos y notas: {}".format(dicc_notas))
print(" ")

#Mostra alumnos y notas
for nombre,nota in dicc_notas.items():
    print(f"{nombre} tiene la nota de {nota}")

#Media de las notas
media = sum(dicc_notas.values()) / num_alum
print("La media de las notas es: {}".format(media))




