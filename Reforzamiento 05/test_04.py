"""
Módulos

4. Creando un archivo principal donde llamará a un módulo (operaciones.py)
el cuál contendrá las siguientes funciones:

-La primera función cargará a 3 números enteros que pedirá al usuario
que ingrese por consola un valor.
-La segunda función solamente sumará dos valores.
-Desde el archivo principal importar al módulo y sumar dos valores
usando las funciones anteriormente creadas en el módulo.
"""

import operaciones_02

# Numeros
numeros = operaciones_02.num_ingresar()

# Sumar valores
operaciones_02.sumar(numeros)
