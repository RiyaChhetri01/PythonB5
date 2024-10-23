class Animal:
   # Constructor (initializer)
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age
    
    
    # Another instance method
    def get_age(self):
        return f"{self.name} is {self.age} years old."