"""Reforzamiento 04"""

"""Diccionarios: Ejercicio 08"""

"""8. Crear una agenda basada en un diccionario donde los key serán los nombres
de las personas y sus “values” serán los números de teléfono de c/u.
Ingresarás por consola el nombre y el número de cada persona que serán
registrados en la agenda.
El programa también te permitirá buscar por nombre en el diccionario en caso
no exista mostrar un mensaje de “No se encuentra registrado en la agenda”. """

#Diccionario
agenda = { }

#Número de personas a registrar
num_person = int(input("Ingresar el número de personas que desea registrar: "))

##Ingresar datos
for i in range(num_person):
    nombre = input(f"Ingrese nombre {i+1}: ")
    telf = float(input(f"Ingrese su telefono {i+1}: "))
    agenda[nombre] = telf

#Busqueda en la agenda
persona = input("Ingrese el nombre a buscar: ")
if persona in agenda:
    print(f"{persona} tiene el número: {agenda[persona]}")
else:
    print("No se encuentra registrado en la agenda.")
