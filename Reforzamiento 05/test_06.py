"""
Decoradores

6.	Crear una función decoradora que dará los buenos días antes de ejecutar
una función a ser decorada “Buenos días NOMBRE son las HORA horas con MINUTOS minutos”
y luego de ser ejecutada lanzará un mensaje diciendo “Hasta luego que tenga buen día”.

- La función a decorar pedirá el nombre de una persona y retornará el mensaje.

"""

from datetime import datetime

# Funcion decoradora

def funcion_decorador(funB):
    def funcC():
        hora_actual = datetime.now()
        hora = hora_actual.hour
        minutos = hora_actual.minute
        nombre = input("Ingresar el nombre: ")
        print(f"Buenos días {nombre} son las {hora} horas con {minutos} minutos")

        funB()

        print("Hasta luego que tenga buen día")
    return funcC

@funcion_decorador
def saludo():
    nom = input("Ingresa un nombre, por favor: ")

saludo()
