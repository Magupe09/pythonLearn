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


num1 = 2+3j
num2= complex(2,3)
print(num2.real,num2.imag)


#Build function
print(abs(5.5))
print(round(5.5))

#Enums
from enum import Enum
class State(Enum):
    INACTIVE=0
    ACTIVE =1
print(State.ACTIVE.value)
print(State(1))
print(list(State))
# Control statemens
condition= True
name = "richard"
if condition == True:
    print("Is true")
elif name == "richard":
    print("Is richard")
else :
    print("condition is false:")

 
dogs0=[] # print("roger" in dogs) = False
dogs=["roger",1,"syd",True]
#print("roger" in dogs)
#print(dogs[0])
dogs[2]="Mauro"
#print(dogs)
#print(dogs[1:3])
#print(len(dogs))
dogs.append("Juda")
#print(dogs)
dogs.extend(["Juda",5])
print(dogs)
dogs.remove("Mauro")
print(dogs)
print(dogs.pop())


items=["roger",1,"syd",True]
items.insert(2,"Test")
items[1:1]=["Test1","Test2"]
print(items) 

#SORTING LISTS
itemsCopi=items[:]#copia el array
items2=["roger","HELO","syd","HEY"]
items2.sort()
print(items2) 

#TUPLES
#DICTIONARIES
#Sets

set1={"Roger","Syd"}
set2={"Roger"}
intersect=set1 & set2
print(intersect)
#FUNTIONS
def hello(name,age):
    print("hola " + name + " YOu are " + str(age) + "Years old")
    return name


hello("Mauro " ,30 )


def count():
    count =0
    def increment():
        nonlocal count
        count = count +1
        print(count)
    increment()
count()
#print(count())

def count():
    count =0
    def increment():
        nonlocal count
        count = count +1
        return count
    return increment
increment=count()
print(increment())

print(increment())

print(increment())



age=8
print(age.real)
print(age.imag)
print(age.bit_length())

#Objects
items=[1,2,3,4,5]
items.append(6)
items.pop()
items.pop(0)
items.clear()
items.count(1)
#items.index(1)
items.reverse()
items.sort()
items.copy()
items.extend([7,8,9])
items.insert(0,0)
items.remove(0)
items.pop()
print(id(items))



#Loops

for i in range(10):
    print(i,"o")


while i < 10:
    print(i,"oo")
    i +=1

items=["Roger","Syd","Mauro"]
for index,item in enumerate(items):
    print(index,item)
#Classes
class Animal:
    def eat(self,food):
        print(f"{self.name} is eating {food}")
        
class Dog(Animal):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        print("Woof")



roger=Dog("Roger",8) 
roger.eat("Dog food")


#Modules
#import dog
#dog.bark()
from dog import bark
bark()
import math
print(math.pi)
import argparse
parser= argparse.ArgumentParser(
    description="This program prints the name of my dogs"
)
print(parser)


#Acepting arguments
import argparse
parser=argparse.ArgumentParser(
    description='This programan print the name of my dogs'
)
parser.add_argument('-c','--color',metavar='color',required=True,choices={
    'red','yellow'
},help='the color to search for')
args=parser.parse_args()
print(args.color)

#print("Mauro" in name,"aqui estoy")
#print(sorted(name))

#Dictionaries


#Lambda Functions

lambda num : num *2
multiply=lambda a,b : a*b
print(multiply(2,4))

#Map, filter, reduce
numbers=[1,2,3]
def double(a):
    return a*2
result=map(double,numbers)
print(list(result))  


numbers=[1,2,3]
def isEven(n):
    return n%2 == 0
result = filter(isEven,numbers)
print(list(result))

'''
expenses =[
    ('Dinner',80),
    ('Car repair',120)
]
sum= 0
for expense in expenses:
    sum+=expense[1]
print(sum)