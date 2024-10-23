squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)
fruits = ['apple', 'banana', 'cherry']
#Filtering Items in a Dictionary
fruit_dict = {fruit: len(fruit) for fruit in fruits}
print(fruit_dict)
#Inverting a Dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = {value: key for key, value in original_dict.items()}
print(inverted_dict)

