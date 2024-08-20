import random

print(random.randrange(10)) # Random amoung 0 inclusive and 9 inclusive (inclusive, exclusive)

print(random.randint(1, 5)) # Random amoung 1 inclusive and 5 inclusive (inclusive, inclusive)

lista_a = [1, 2, 3, 4, 5]
print(random.choice(lista_a)) # Random amount all list elements inclusive

print(random.sample(lista_a, 3)) # Random return 3 elements from the list

print(random.random()) # Return a float number between 0 inclusive and 1 exclusive (inclusive, exclusive)

print(random.uniform(1, 10)) # Return a float number between 1 inclusive and 10 exclusive

