from random import choice

options = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

result = ""

for value in range(4):
    print(f"price if your ticket have a {choice(options)}")