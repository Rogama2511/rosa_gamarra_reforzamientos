"""Reforzamiento 03"""

"""Ejercicio 09"""

"""9. Crear un programa en Python donde tendrás una lista con 5 departamentos, 
ingresarás 2 departamentos adicionales por posición, el cual el segundo departamento 
estará en la posición ‘1’ y el primero en penúltimo lugar, finalmente mostrar la lista original 
y la lista actualizada en terminal"""

#Lista departamentos
lista_deptamentos = ["Lima", "Amazonas", "Cusco", "Piura", "La Libertad"]

print("Lista original: {}".format(lista_deptamentos))

#Ingresar departamentos
lista_deptamentos.insert(-1, "Huánuco")
lista_deptamentos.insert(1,"Cajamarca")

print("Lista actualizada: {}".format(lista_deptamentos))
