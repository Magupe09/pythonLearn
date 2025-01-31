###
# 02 - Booleanos
# Valores lógicos: True (verdadero) y False (falso).
# Fundamentales para el control de flujo y la lógica en programación.
###
"""
import os
os.system("clear")

# Los booleanos representan valores de verdad: True o False.
print("\nValores booleanos básicos:")
print(True)
print(False)

# Operadores de comparación: devuelven un valor booleano.
print("\nOperadores de comparación:")
print("5 > 3:", 5 > 3)        # True
print("5 < 3:", 5 < 3)        # False
print("5 == 5:", 5 == 5)      # True (igualdad)
print("5 != 3:", 5 != 3)      # True (desigualdad)
print("5 >= 5:", 5 >= 5)      # True (mayor o igual que)
print("5 <= 3:", 5 <= 3)      # False (menor o igual que)

print("\nComparación de cadenas:")
print("'manzana' < 'pera':", "manzana" < "pera") # True
print("'Hola' == 'hola'", "Hola" == "hola") # False

# Operadores lógicos: and, or, not
print("\nOperadores lógicos:")
print("True and True:", True and True)   # True
print("True and False:", True and False)  # False
print("True or False:", True or False)    # True
print("False or False:", False or False)  # False
print("not True:", not True)             # False
print("not False:", not False)            # True

# Tablas de verdad (para referencia):
print("\nTablas de verdad:")
print("\nand:")
print("A     B     A and B")
print("True  True ", True and True)
print("True  False", True and False)
print("False True ", False and True)
print("False False", False and False)

print("\n or:")
print("A     B     A or B")
print("True  True ", True or True)
print("True  False", True or False)
print("False True ", False or True)
print("False False", False or False)

print("\n not:") 
print("A     not A")
print("True ", not True)
print("False", not False)


###
# EJERCICOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
print('solucion')

num1,num2 = map(int,input("Ingresa dos numeros  \n").split())
  
if num1 > num2:
    print(f'{num1} Es el mayor')
elif num1 == num2:
        print(f'son los mismos numeros')
else: 
    print(f'{num2} Es el mayor')    

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

import os
os.system("clear")

print('solucion')
suma = 0
num1,num2 = map(int,input("Ingresa dos numeros  \n").split())

operacion = input("Escoge una operacion a realizar (+, -, *, /) \n").strip()
if operacion == '+' :
   suma = num1 + num2
   print(f'{suma}') 

if operacion == '-' :
   resta = num1 - num2
   print(f'{resta}') 

if operacion == '*' :
   multiplicacion = num1 * num2
   print(f'{multiplicacion}')

if operacion == '/' :
   if num1 and num2 == 0:
    print('No se puede divir entre 0')
   else :
      division = num1 / num2
      print(f'{division}')

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

import os
os.system("clear")

year = int(input("Ingresa un año cualquiera y te digo si es bisiesto  \n"))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f'{year} es bisiesto')
else :
    print(f'{year} No es bisiesto')    

"""
# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)


import os
os.system("clear")

edad = int(input("Ingresa tu edad  \n"))


if  edad <= 2:
   print(f'{edad} Eres un bb')
elif edad >= 3 and edad <= 12 :
    print(f'{edad} Eres un Niño')
    
elif edad >= 13 and edad <= 17 :
    print(f'{edad} Eres adolocente ')

elif edad >= 18 and edad <= 64 :
    print(f'{edad} Eres un Adulto')

elif edad > 65 :
    print(f'{edad} Eres adulto mayor ')
