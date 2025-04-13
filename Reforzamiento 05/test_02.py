"""
Módulos

2. Creando un archivo principal (main.py) donde importará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones:
- Una función que realizará la carga de un valor entero y que verifique
que solamente tiene que ser numérico
- Una función que mostrará por pantalla la raíz cuadrada de dicho valor
- Y otra función el valor elevado al cuadrado y al cubo de dicho número,
puedes devolver un diccionario
- Utilizar el módulo math de python

"""
import operaciones

numero = operaciones.ingresar_num()

#Realizar las operaciones
print("La raíz cuadrada de {} es: {:.3f}".format(numero,operaciones.raiz(numero)))

resultados = list(operaciones.elevar(numero))
print("El cuadrado de {} es: {}".format(numero,resultados[0]))
print("El cubo de {} es: {}".format(numero,resultados[1]))

