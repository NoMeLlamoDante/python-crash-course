print("Give me two numbers, and i'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFisrt number: ")
    if first_number == 'q':
        break
    secon_number = input("\nSecond number: ")
    if secon_number == 'q':
        break
    try:
        answer = int(first_number)/int(secon_number)    
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer) 