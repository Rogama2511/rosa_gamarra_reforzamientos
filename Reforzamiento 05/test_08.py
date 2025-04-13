"""
Decoradores

8.	Crear un decorador donde imprimirá la cantidad de argumentos que tiene
la función a decorar usando *args y **kwargs.
Mensaje previo “La cantidad de argumentos que tiene la función es {}”
mensaje post “La función decoradora terminó de ejecutarse correctamente”

Ejemplo: Al usar una función suma que creamos y usamos
suma(4, 1, 10, 2, 50, 64)
El decorador determinará la cantidad de argumentos que tiene la función al decorarla.

Salida:
“La cantidad de argumentos que tiene la función es”
5
“La función decoradora terminó de ejecutarse correctamente”

"""

def fun_decorator(funcB):
    def funcionC(*args, **kwargs):
        cant_args = len(args) + len(kwargs)
        print("La cantidad de argumentos que tiene la función es {}".format(cant_args))
        result = funcB(*args, **kwargs)
        print("La función decoradora terminó de ejecutarse correctamente")
        return result
    return funcionC

@fun_decorator
def sumar(*args, **kwargs):
    valores = kwargs.values()
    resultado = sum(args) + sum(valores)
    print("El resultado de la suma: {}".format(resultado))
    return resultado

sumar(4, 1, 10, 2, b = 50, c = 64)
