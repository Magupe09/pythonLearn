#Decorators

def logtime(func):
    def wrapper():
        # do something before
        print("before")
        val = func()
        # do something after
        print("after")
        return val
    return wrapper

@logtime
def hello():
    print("helloo")

hello()
#DocstRINGS

def increment(n):
    """ Increment a number """
    return n+1

class Dog:
    """ A class representing a dog """
    def __init__(self,name,age):
        """ Initialize a new dog """
        self.name = name
        self.age= age
    def bark(self):
        """ Let the dog bark """
        print("WOF!")

        