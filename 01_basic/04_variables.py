###

# 04-variables
#Las variables sirven para guardar datos en memoria
# Python es un lenguaje de tipado dinamico y de tipado fuerte

###

# Para asignar una variable
# solo hace falta poner esto;

my_name="MAGUPE"

print(my_name)

#Tipado dinamico: El tipo de dato se determina en tiempo de ejecucion
#que no tienes que declararlo explicitamente
age ="maguep"
print(age)

age=32
print(age)

#Tipado Fuerte: No realiza conversiones de tipo automatico

# f-string (literal de cadena de formato)
print(f"Hola mundo {my_name}, tengo {age}")
# NO recomendada de asignar variables

name,age,city = "MARU",32,"bOGOTA"

#Convecines de nombres variables
mi_nombre_de_variable ="ok" #snake_case
nombre="ok"

MiNombreDeVariable = "ok"
minombredevariable ="ok"

MI_CONSTANTE = 3.14 # UPPER_CASE => constantes

#FORMAS DE NO VALIDOS EN VARIABLES

#123_variable ="ok"
#mi-variable = "ok"
#mi variable = "ok"