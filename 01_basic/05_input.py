###

# 05-INput  Entrada de datos al usuario

# Puedes obtener datos al usuario en la consola

###


#nombre=input("hola como te llamas? \n")
#print(f"hola {nombre}")

#Para obtener multiples valores

print("Obtener multiples valores a la vez")
country, city = input("En que pais vives? \n").split()

print(f"vives en {country},{city}")