#4-1
pizzas = ['Hawaian', 'Honolulu', '4 cheeses', 'meat lover']

for pizza in pizzas:
    print(f"I really love {pizza.title()} pizza!")

#4-2 
animals = ['black panther', 'lion', "tiger"]

for animal in animals:
    print(f"a {animal.title()} is a bigger cat")

#4-3
for value in range(1,21):
    print(value)
    
#4-4 
one_million_values = [value for value in range(1,1_000_001)]
print(one_million_values)

#4-5
print(f"min: {min(one_million_values)}")
print(f"max: {max(one_million_values)}")
print(f"sum: {sum(one_million_values)}")

#4-6 odd numbers
odd_numbers = [value for value in range(1,21,2)]
for odd_number in odd_numbers:
    print(odd_number)

#4-7 threes
multiples = [value*3 for value in range(1,11)]
for multiple in multiples:
    print(multiple)
    
#4-8 cubes
cubes = []
for value in range(1,11):
    cubes.append(value**3)
for cube in cubes:
    print(cube)

#4-9
cubes = [value**3 for value in (range(1,11))]
print(cubes)

#4-10 Slices
my_foods = ['pizza', 'falafel', 'carrot cake']
my_foods.append('cannoli')
my_foods.append('ice cream')

print("The first three items in the list are:")
print(my_foods[:3])

print("Three items from the middle:")
print(my_foods[1:4])

print("The last three items in the list are:")
print(my_foods[-3:])

#4-11 My pizza, Your pizzas
pizzas = ['Hawaian', 'Honolulu', '4 cheeses', 'meat lover']

friend_pizzas = pizzas[:]

pizzas.append("pastor")
friend_pizzas.append("margerita")

print("My favorite pizzas are:")
print(pizzas)

print("My friend's favorite pizzas are:")
print(friend_pizzas)

#4-12 More loops

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(food.title())
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food.title())
    
#4-13 Buffet
foods = ('hamburguer', 'sushi', "spaguetti", "croissant", "shawarma")

print("\nThe actual buffet:")
for food in foods:
    print(food.title())

foods = ('hamburguer', 'sushi', "bolognese", "taco", "shawarma")
print("\nThe new buffet:")
for food in foods:
    print(food.title())
    
#4-14 PEP8

#4-15

#4-12 More loops
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(food.title())

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food.title())