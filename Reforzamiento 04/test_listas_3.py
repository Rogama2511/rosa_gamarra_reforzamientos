"""Reforzamiento 04"""

"""Listas: Ejercicio 03"""

"""3. Tienes una lista con 5 nombres de estudiantes. Crear un programa que te
pedirá ingresar el nombre de un estudiante, la cuál será eliminada de lista
inicial en caso que no exista en la lista mostrar un mensaje donde indique
que no se encuentre en la lista y esta será agregada a la lista.
 Finalmente mostrar la lista actualizada en consola."""

#Lista nombres
list_nombres = ["Juan", "Pedro", "Lucia", "Maria", "Lina"]
print("Lista inicial de nombres: {}".format(list_nombres))

#Ingresar nombre
nombre = input("Ingrese nombre del estudiante: ")

#Eliminar o agregar ala lista
if nombre in list_nombres:
    list_nombres.remove(nombre)
    print("El nombre {} ha sido eliminado de la lista".format(nombre))
else:
    list_nombres.append(nombre)
    print("El nombre {} no se encontra en la lista y sera agregado".format(nombre))

#Lista actualizada
print("Lista de nombres actualizada: {}".format(list_nombres))

