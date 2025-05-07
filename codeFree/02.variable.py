name = ("Mauro","Jan","pepito")
print(name)

age=12
# age=float(12)
# age=int("20")
print(age)
print(isinstance(name,str)) # print(isinstance(age,int)),print(isinstance(age,float))

'''
complex for complex numbers
bool for booleans
list for lists
tuple for tuples
range for ranges
dict for dictionaries
set for sets
'''
## OPERATORS 

age=8
age +=8
print(age)

division = 4 // 2  
#print(division)
a=1
b=2
a == b #false
a != b #true
a > b #false 
a <= b #true

condition1=True
condition2=False

not condition1 #false
condition1 and condition2 #false
condition1 or condition2 #true

def is_adult(age):
    if age > 18:
        return True
    else: return False

def is_adult2(age):
    return True if age > 18 else False

#strings

"Beau"
'Beau'
name = "Beau"
phrase = name + "  Is my name"
print("beau".lower())
print("beau".upper())
print("beau".title())







#print("Mauro" in name,"aqui estoy")
#print(sorted(name))

#Dictionaries
 