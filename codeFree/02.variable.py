name = ("Mauro","Jan","pepito")
print(name)

age=12
# age=float(12)
# age=int("20")
#print(age)
#print(isinstance(name,str)) # print(isinstance(age,int)),print(isinstance(age,float))

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
'''
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
name1="Mauro"
phrase = name + "  Is my name"
print("beau".lower())#Minusculas
print("beau".upper())#Mayusculas
print("beau".title())#Convierte la primera letra en mayusculas para titulos
print(name1[1:2])
print("au" in name)

'''
#Booleans

done = True
done = False
print(type(done)==bool)
if done:
    print("Yes")
else:
    print("No")

book_1_read = False
book_2_read = False

read_any_book=any([book_1_read,book_2_read])
print(read_any_book)

ingredients_purchased = True
meal_cooked = False

ready_to_serve = all([ingredients_purchased,meal_cooked])
print(ready_to_serve)



#print("Mauro" in name,"aqui estoy")
#print(sorted(name))

#Dictionaries
 