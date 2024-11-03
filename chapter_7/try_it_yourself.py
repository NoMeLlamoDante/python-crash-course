#7-1 Rental Cars
promt = "Welcome to rental carl's, which car do you want to rent? "
car = input(promt)
print(f"Let me see you if I can find you a {car.title()}")

#7-2 Restaurant Seating
promt = "Welcome to pujol, how many people comes with you? "
customers = input(promt)
customers = int(customers)
if customers > 8:
    print("please, wait a moment until we can have your table")
else: 
    print("come here, your table is ready")

#Multiple of Ten
promt = "Please, enter a number: "
number = input(promt)
number = int(number)
if number % 10 == 0:
    print(f'{number} is multiple of 10')
else:
    print(f'{number} is not a multiple of 10')