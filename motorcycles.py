# motorcycles = ['honda','yamaha','suzuki']
# print(motorcycles)
# #Editing
# # motorcycles[0] = 'ducati'
# # print(motorcycles)

# # Appending
# motorcycles.append('ducati')
# print(motorcycles)

# motorcycles = []

# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# print(motorcycles)

#insert
# motorcycles.insert(0,'ducati')
# print(motorcycles)

#delete
# del motorcycles[1]
# print(motorcycles)

#pop
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

# last_owned = motorcycles.pop()
# print(f"The last motorcycle I owned was a {last_owned.title()}")

# first_owned = motorcycles.pop(0)
# print(f"The first motorcycle I owned was a {first_owned.title()}")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

# motorcycles.remove('ducati')
# print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)

print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me")