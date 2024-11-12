# 10 - 6 Addition

first_number = input('Insert the first number: ')
second_number = input('Insert the second number: ')

try: 
    first_number = int(first_number)
    second_number = int(second_number)
    result = first_number + second_number
except ValueError:
    print("any data is invalid")
else: 
    print(f"{first_number} + {second_number} = {result}")