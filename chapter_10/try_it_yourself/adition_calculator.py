# 10 - 6 Addition

def calculator():
    while True:
        prompt = "Insert a number: (enter 'q' to exit) "
        first_number = input(prompt)
        if first_number == 'q':
            break
        second_number = input(prompt)
        if second_number == 'q':
            break
        try: 
            first_number = int(first_number)
            second_number = int(second_number)
            result = first_number + second_number
        except ValueError:
            print("any data is invalid")
        else: 
            print(f"{first_number} + {second_number} = {result}")

calculator()