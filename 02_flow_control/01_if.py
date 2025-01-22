###
#01-sentencias condicionales (if,elif,else)
#permiten ejecutar bloques de codigo solo si se cumple ciertas condiciones

###

import os
os.system("clear")

print("\n sentencia simple condicional")

edad = 18

if edad >= 18:
    print("Eres mayor de edad")



print("\n sentencia simple condicional con else")


if edad >= 18:
    print("Eres mayor de edad")
else: 
    print("eres menor de edad")


print("\n sentencia simple condicional con elif")
nota = 7
if nota >= 9:
    print("sobresaliente")

elif nota >= 7:
    print("Notable")
else : 
    print("No tienes nota")


print("\n condicionales multiples")
edad =18
tiene_carnet = True

#javascripr
#&& => and
#|| => or

if edad >= 18 and tiene_carnet:
    print("puedes conducir")
else:
    print("policia")


#En un pueblo extraño

if edad >= 18 or tiene_carnet:
    print("puedes conducir ")
else:
    print("paga al policia y de dejan conducir")

es_fin_de_semana = False

if not es_fin_de_semana:
    print("Mao hay que estudiar ")


print("\n andidar condicionales")

edad = 20
tiene_dinero =True

if edad >= 18:
    if tiene_dinero:
       print("puedes ir a la disco")
    else:
     print("Quedate en casa")
else:
    print("No eres mayor")