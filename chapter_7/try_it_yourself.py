#7-1 Rental Cars
prompt = "Welcome to rental carl's, which car do you want to rent? "
car = input(prompt)
print(f"Let me see you if I can find you a {car.title()}")

#7-2 Restaurant Seating
prompt = "Welcome to pujol, how many people comes with you? "
customers = input(prompt)
customers = int(customers)
if customers > 8:
    print("please, wait a moment until we can have your table")
else: 
    print("come here, your table is ready")

#Multiple of Ten
prompt = "Please, enter a number: "
number = input(prompt)
number = int(number)
if number % 10 == 0:
    print(f'{number} is multiple of 10')
else:
    print(f'{number} is not a multiple of 10')

#7-4 Pizza Toppigs
prompt = "Please, enter the pizza topping you choice: "
prompt += "(enter 'quit' for exit). "

while True:
    topping = input(prompt)
    
    if topping == 'quit':
        break
    else: 
        print(f'\tadding {topping.title()} to your pizza')

#7-5 Movie Tickets
prompt = "Welcome to cinepolis, please insert your age:"
prompt+= "(insert 0 to close) "

age = 1

while age != 0:
    age = input(prompt)
    age = int(age)

    if age == 0:
        continue
    elif age < 3:
        print("Your ticket is free")
    elif age >= 3 and age <=12:
        print("Your ticket is $10")
    elif age >12:
        print("Your ticket is $15")

#7-6 Three Exits
prompt = "Welcome to cinepolis, please insert your age:"
prompt+= "(insert 0 to close) "

age = 1

while age != 0:
    age = input(prompt)
    age = int(age)

    if age == 0:
        continue
    elif age < 3:
        print("Your ticket is free")
    elif age >= 3 and age <=12:
        print("Your ticket is $10")
    elif age >12:
        print("Your ticket is $15")

while True:
    age = input(prompt)
    age = int(age)

    if age == 0:
        break
    elif age < 3:
        print("Your ticket is free")
    elif age >= 3 and age <=12:
        print("Your ticket is $10")
    elif age >12:
        print("Your ticket is $15")
        
tickets_remaining = 5
while tickets_remaining > 0:
    tickets_prompt = f"tickets = {tickets_remaining}\n"
    age = input(prompt+tickets_prompt)
    age = int(age)

    if age == 0:
        tickets_remaining = 0
    elif age < 3:
        print("Your ticket is free")
        tickets_remaining-=1
    elif age >= 3 and age <=12:
        print("Your ticket is $10")
        tickets_remaining-=1
    elif age >12:
        print("Your ticket is $15")
        tickets_remaining-=1
#7-7 Infinity 
# while True: 
#     print("press CTRL+C to close")
    
    
#7-8
sandwich_orders = ['peperoni', 'tuna', 'ham & cheese']
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"I made your {order} sandwitch")
    finished_sandwiches.append(order)

print("made sandwitches")
for sandwitch in finished_sandwiches:
    print(f"\t{sandwitch}")

#7-9 No Pastrami
sandwich_orders = ['pastrami', 'peperoni', 'pastrami', 
                'tuna', 'pastrami', 'ham & cheese', 'pastrami']
finished_sandwiches = []

print("\nThe deli has out of pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"I made your {order} sandwitch")
    finished_sandwiches.append(order)

print("made sandwitches")
for sandwitch in finished_sandwiches:
    print(f"\t{sandwitch}")
    
#7-10 Dream vacation
places = {}
prompt = 'If you would visit one place of the world, where would you go? '

flag = True

while flag:
    name = input("What's your name? ")
    place = input(prompt)
    places[name] = place
    
    repeat = input("would you like add another person data? (Yes/No) ")
    if repeat == 'no':
        flag=False

print("There are the results from the poll: ")
for name, place in places.items():
    print(f"\t{name.title()}: {place.title()}")