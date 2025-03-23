"""Reforzamiento 03"""

"""Ejercicio 02"""

"""2. Devuelve la cantidad de veces que se repite un curso que hayas llevado en pregrado 
(agregarlos previamente a la lista con un mínimo de 5 cursos) luego mostrarla, finalmente 
elimina el segundo ítem de la lista usando debidamente su índice y mostrar en consola tu lista actualizada"""

cursos = ["Mecánica Clásica", "Electromagnetismo", "Termodinámica", "Mecánica Cuántica"]

cursos.append("Óptica")
cursos.append("Física Moderna")
cursos.append("Mecánica Cuántica")
cursos.append("Mecánica Cuántica")

#Cantidad de veces que se repite "Mecánica Cuántica"
print("El curso 'Mecánica Cuántica' se repite {} veces".format(cursos.count("Mecánica Cuántica")))
print("Lista de cursos: {}".format(cursos))

#Eliminar el segundo ítem
cursos.pop(1)

#Lista actualizada
print("Lista actualizada: {}".format(cursos))
