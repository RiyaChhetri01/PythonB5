#from dog import Dog
#from cat import Cat
class Dog:

    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    # Constructor (initializer)
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age
    
    # Instance method
    def bark(self):
        return f"{self.name} says woof!"
    
    # Another instance method
    def get_age(self):
        return f"{self.name} is {self.age} years old."
# Creating instances (objects) of the Dog class

dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)#Accessing attribute and methods 

print(dog1.bark())         # Buddy says woof!
print(dog2.get_age())      # Charlie is 5 years old.
print(dog1.species)        # Canis familiaris
 
print("-----------------------")
class Cat:

    # Class attribute (shared by all instances)
    species = "Canis Species"
    
    # Constructor (initializer)
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age
    
    # Instance method
    def sound(self):
        return f"{self.name} says meow!"
    
    # Another instance method
    def get_age(self):
        return f"{self.name} is {self.age} years old."
# Creating instances (objects) of the Dog class

cat1 = Cat("Buddy", 3)
cat2 = Cat("Charlie", 5)#Accessing attribute and methods 

print(cat1.sound())         # Buddy says woof!
print(cat2.get_age())      # Charlie is 5 years old.
print(cat1.species)        # Canis familiaris

print("---------------")
class Animal:
   # Constructor (initializer)
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age
    
    
    # Another instance method
    def get_age(self):
        return f"{self.name} is {self.age} years old."
# Creating instances (objects) of the Dog class
class Dog(Animal):
    species = "Canis Species"

    def bark(self):
        return f"{self.name} says woof!"
    
class CAt(Animal):
    species = "Canis Species"

    def sound(self):
        return f"{self.name} says meow!"
     
     
        
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)#Accessing attribute and methods 
cat1 = Cat("Buddy", 3)
cat2 = Cat("Charlie", 5)#Accessing attribute and methods 

      # Canis familiaris

print(dog1.bark())         # Buddy says woof!
print(dog2.get_age())      # Charlie is 5 years old.
print(dog1.species)  
print(cat1.sound())         # Buddy says woof!
print(cat2.get_age())      # Charlie is 5 years old.
print(cat1.species)        # Canis familiaris
