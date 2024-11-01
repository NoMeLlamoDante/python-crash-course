#5-1 Conditional Test
car = 'lexus'
#1
print("Is car == 'subaru'?, I predict True.")
print(f"car: {car.title()}")
if car.lower() == 'subaru':
    print("I've Won")
else:
    print("I failed")
#2
print("\nIs car == 'audi'?, I predict False.")
print(f"car: {car.title()}")
if car.lower() == 'audi':
    print("I failed")
else:
    print("I've Won")
#3
print("\nIs car != 'lexus'?, I predict False.")
print(f"car: {car.title()}")
if car.lower() != 'lexus':
    print("I failed")
else:
    print("I've Won")
#4 
print("\nIs car != 'nissan'?, I predict True.")
print(f"car: {car.title()}")
if car.lower() != 'nissan':
    print("I've Won")
else:
    print("I failed")
#5
print("\nIs car != 'subaru' and car != 'toyota'? , I predict True.")
print(f"car: {car.title()}")
if car.lower() != 'subaru' and car.lower() != 'toyota':
    print("I've Won")
else:
    print("I failed")
#6
print("\nIs car != 'lexus' and car != 'nissan'?, I predict False.")
print(f"car: {car.title()}")
if car.lower() != 'lexus' and car.lower() != 'nissan':
    print("I failed")
else:
    print("I've Won")
cars = ['nissan', 'toyota', 'lexus']
#7
print("\nIs car in cars list?, I predict True.")
print(f"car: {car.title()}")
print(f"cars list: {cars}")
if car in cars:
    print("I've Won")
else:
    print("I failed")
#8
print("\nIs car in cars list?, I predict False.")
print(f"car: {car.title()}")
print(f"cars list: {cars}")
if car in cars:
    print("I failed")
else:
    print("I've Won")
#9
print("\nIs not car in cars list?, I predict True.")
print(f"car: {car.title()}")
print(f"cars list: {cars}")
if car not in cars:
    print("I've Won")
else:
    print("I failed")
#10
print("\nIs not car in cars list?, I predict False.")
print(f"car: {car.title()}")
print(f"cars list: {cars}")
if car not in cars:
    print("I failed")
else:
    print("I've Won")
    
#5-2 More Conditional Test
number = 10

if number > 5 and number < 20:
    print(f"{number} is bigger than 5 and lower than 20")

if number == 5:
    print(f"the number is five")

if number <= 10:
    print(f"the number is lower than 11")

if number != 10 and number < 20:
    print(f"number is lower than 20 and different than 10")

if number > 5 or number == 20:
    print(f"number is 20 or lower than 5")

#5-3 Alien colors #1
alien_color = 'green'

if alien_color == "green":
    print('player earn 5 points')


alien_color = 'yellow'

if alien_color == "green":
    print('player earn 5 points')
    
#5-4 Alien colors #2
alien_color = 'yellow'

if alien_color == "green":
    print('player earn 5 points')
else:
    print('player earn 10 points')

alien_color = 'green'

if alien_color == "green":
    print('player earn 5 points')
else:
    print('player earn 10 points')

#5-5 Alien Colors #3
alien_color = 'green'

if alien_color == "green":
    print('player earn 5 points')
elif alien_color == "yellow":
    print('player earn 10 points')
elif alien_color == 'red':
    print('player earn 15 points')

alien_color = 'yellow'

if alien_color == "green":
    print('player earn 5 points')
elif alien_color == "yellow":
    print('player earn 10 points')
elif alien_color == 'red':
    print('player earn 15 points')


alien_color = 'red'

if alien_color == "green":
    print('player earn 5 points')
elif alien_color == "yellow":
    print('player earn 10 points')
elif alien_color == 'red':
    print('player earn 15 points')

#5-6 Stages of Life
age = 31

if age < 2:
    print("baby")
elif age >= 2 and age < 4:
    print("toddler")
elif age >= 4 and age < 13:
    print("kid")
elif age >= 13 and age < 20:
    print("teenager")
elif age >= 20 and age < 65:
    print("adult")
elif age >= 65: 
    print("elder")

#5-7 Favorite fruit
favorite_fruits = ['tangerine', 'apple', 'grapes']

fruit = 'pineaple'
if fruit in favorite_fruits:
    print(f"You really like {fruit}!")
fruit = 'tangerine'
if fruit in favorite_fruits:
    print(f"You really like {fruit}!")
fruit = 'mango'
if fruit in favorite_fruits:
    print(f"You really like {fruit}!")
fruit = 'grapes'
if fruit in favorite_fruits:
    print(f"You really like {fruit}!")
fruit = 'watermelon'
if fruit in favorite_fruits:
    print(f"You really like {fruit}!")

#5-8 Hello Admin
users = ['alice', 'dante', 'concord', 'admin', 'lucious']

for user in users:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging again")
        
#5-9 No Users:
users = []
if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging again")
else: 
    print("We need to find some users!")

#5-10 Checking Usernames
current_users = ['andrew', 'carolina', 'david', 'ania', 'borja']
new_users = ['panda', 'carly', 'ania', 'lazarus', 'andrew']

for new_user in new_users:
    lower_users = [user.lower() for user in current_users]
    if new_user.lower() in lower_users:
        print(f"username: {new_user.title()} is taken, please enter a new username")
    else: 
        print(f"username: {new_user.title()} is available")
    
#5-11 Ordinal Numbers
numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    elif number > 3 and number <= 9:
        print(f"{number}th")
        
#5-12
numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    elif number > 3 and number <= 9:
        print(f"{number}th")

#5-13 Your ideas
existences = ['acetaminophen', 'metformin', 'ibuprofen', 'telmisartan']
prescripted_pills = ['calcium', 'metformin', 'ibuprofen', 'aspirin']

supply = []
order = []

#Process
for pill in prescripted_pills:
    if pill in existences:
        supply.append(pill)
    else: 
        order.append(pill)

#Supply pills
if order: 
    print("we have this pills for you:")
    for pill in supply:
        print(pill.title())
else:
    print("we don't have any pills for you, sorry")

#Order pills
if order:
    print(f"pills we need: {order}")

