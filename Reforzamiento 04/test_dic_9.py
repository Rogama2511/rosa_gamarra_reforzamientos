"""Reforzamiento 04"""

"""Diccionarios: Ejercicio 09"""

"""9. Una empresa desea gestionar las facturas pendientes que tiene por pagar,
para esto se creará un diccionario donde tendrá por key el número de factura
“00054” y su value será el coste de la factura. El programa tendrá la opción
de pedir nueva factura (por consola) que se agregará al diccionario. Cada vez
que el área de contabilidad pague una factura se pedirá el número de factura
que fue cancelada, si existe mostrar un mensaje donde indicará “La factura
ya está cancelada” caso contrario “El número de factura no existe”
Considerar que cada vez que se realice algún pago o ingreso de una nueva
factura se mostrará inmediatamente al diccionario actualizado. """

#Diccionario facturas
dicc_factur = {
    "03054": 250.75,
    "00123": 480.50,
    "10289": 320.00,
    "50345": 150.25 }

#Ingresar opcion a realizar facturas
print("Ingrese que desea hacer: (a) Factura nueva (b) Pagar factura")

opcion = input("Ingresa la opcion: ")
if opcion == "a":
    num_factura = input("Ingrese número de factura: ")
    if num_factura in dicc_factur:
        print("El número de factura ya existe")
    else:
        costo = float(input("Ingrese costo: "))
        dicc_factur[num_factura] = costo
        print("Factura agregada")
elif opcion == "b":
    num_factura = input("Ingrese factura a cancelar:")
    if num_factura in dicc_factur:
        print("Factura cancelada")
    else:
        print("Factura no existe")
else:
    print("Opcion no valida")

#Mostrar facturas
print("El diccionario de facturas es: {}".format(dicc_factur))
