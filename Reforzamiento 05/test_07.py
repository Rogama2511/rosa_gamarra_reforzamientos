"""
Decoradores

7.	Haciendo el uso de *args y **kwargs aplicarlo debidamente para decorar decorar
una función que recibirá 6 argumentos los cuales se multiplicarán entre ellos
(3 de ellos serán usados con **kwargs)

Mensaje previo al usar el decorador “Está por ejecutarse la función”
y mensaje luego de usar el decorador “La función ha sido ejecutado correctamente”

"""

def fun_decorador(funcB):
    def funcC(*args, **kwargs):
        print("Está por ejecutarse la función")
        result = funcB(*args, **kwargs)
        print("La función ha sido ejecutada correctamente")
    return funcC

@fun_decorador
def multiplicar(num1, num2, num3, **kwargs):
    num4, mun5, mun6 = kwargs.values()
    result = num1 * num2 * num3 * num4 * mun5 * mun6
    print("El resultado de la multiplicación: {}".format(result))


multiplicar(1,2,3, a = 3, b = 4, c = 5)
