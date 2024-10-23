from dog import Dog
from cat import Cat

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
