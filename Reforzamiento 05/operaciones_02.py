"""
Para test_04
-La primera función cargará a 3 números enteros que pedirá al usuario
que ingrese por consola un valor.
-La segunda función solamente sumará dos valores.
-Desde el archivo principal importar al módulo y sumar dos valores
usando las funciones anteriormente creadas en el módulo.
"""
def num_ingresar():
    numeros = []
    try:
        for i in range(1,4):
            numero = int(input("Ingrese el número {}:".format(i)))
            numeros.append(numero)
    except TypeError:
        print("Ingrese solo números enteros")
    return numeros


# Suma
def sumar(numeros):
    print("a) 1° + 2°   b) 2° + 3°  c) 1° + 3° ")
    opcion = input("Escoge que números quiere sumar:")
    if opcion == "a":
        suma = numeros[0] + numeros[1]
        print("La suma es: {}".format(suma))
    elif opcion == "b":
        suma = numeros[1] + numeros[2]
        print("La suma es: {}".format(suma))
    else:
        suma = numeros[0] + numeros[2]
        print("La suma es: {}".format(suma))
    return suma

