#6-1 Person
person = {'name': 'gilberto',
        'last_name': 'salazar',
        'age': 35,
        'city': 'british Columbia'}

print(f"My friend {person['name'].title()} {person['last_name'].title()}," +\
    f"has {person['age']} years and lives in {person['city'].title()}")

#6-2 Favorite Numbers
favorite_numbers = {
    'miguel': 5, 
    'frigo': 15,
    'jaime': 8,
    'manu': 24,
    'adrian': 10
}

print(f"miguel's favorite number: {favorite_numbers['miguel']}")
print(f"frigo's favorite number: {favorite_numbers['frigo']}")
print(f"jaime's favorite number: {favorite_numbers['jaime']}")
print(f"manu's favorite number: {favorite_numbers['manu']}")
print(f"adrian's favorite number: {favorite_numbers['adrian']}")

#6-3 Glossary
glossary = {
    'programing': 'the process or activity of writing computer programs',
    'pixel': "a minute area of ilumination on a display screen, " +\
            "one of the many from which an image is composed",
    'game': 'an activity that one engages in for amusement of fun',
    'list': 'a number of conected items or names written or printed consecutively',
    'python': 'a high-level general-purpose programing language'
}

print(f"Programing: '{glossary['programing']}'\n")
print(f"Pixel: '{glossary['pixel']}'\n")
print(f"Game: '{glossary['game']}'\n")
print(f"List: '{glossary['list']}'\n")
print(f"Python: '{glossary['python']}'\n")

#6-4 Glossary 2
glossary['key'] = 'enter or operate on (data) by means of a ' +\
                    'computer keyboard or telephone keypad'
glossary['value'] = 'the meaning of a word or other linguistic unit.'
glossary['collection'] = 'a group of things or something'
glossary['loop'] = 'a structure, series, or process, the end of which is' +\
                    'connected to the begining'
glossary['sorted'] = 'the arrangement of data in a prescribed sequence'

for word, meaning in glossary.items():
    print(f"{word.title()}: {meaning.capitalize()}")
    
#6-5 Rivers
rivers = {'senna': 'france', 'nilo': 'egypt', 'plate': 'argentina', 'bravo': 'méxico'}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)
    
#6-6 Polling
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

poll_names = ['joseph', 'edward', 'sarah', 'bernard', 'bianca']

for name in poll_names:
    if name not in favorite_languages.keys():
        print(f"{name.title()},Please take the poll")
    else: 
        print(f"{name.title()}, Thanks for answer the poll")

# 6-7 People
person_0 = {
    'name': 'gilberto',
    'last_name': 'salazar',
    'age': 35,
    'city': 'british Columbia'
}

person_1 = {
    'name': 'cihua',
    'last_name': 'vidal',
    'age': 31,
    'city': 'Ostrava'
}

person_2 = {
    'name': 'carlos',
    'last_name': 'roan',
    'age': 58,
    'city': 'ontario'
}

people = (person_0, person_1, person_2)

for person in people:
    full_name = f"{person['name']}, {person['last_name']}"
    print(f"My friend {full_name.title()}, has {person['age']} years " +
        f"and lives in {person['city'].title()}")

# 6-8 Pets
pet_0 = {
    'name': 'moon',
    'spiece': 'cat',
    'owner': 'rodri',
    'age': 5
}

pet_1 = {
    'name': 'randy',
    'spiece': 'dog',
    'owner': 'may',
    'age': 12
}

pet_2 = {
    'name': 'dogo',
    'spiece': 'dog',
    'owner': 'joshua',
    'age': 8
}

pet_3 = {
    'name': 'garfield',
    'spiece': 'cat',
    'owner': 'john',
    'age': 6
}

pets = (pet_0, pet_1, pet_2, pet_3)

for pet in pets:
    for data, value in pet.items():
        print(f"{data.title()}: {value}")
    print()

#6-9 Favorite places
favorite_places = {
    'auron': ['spain', 'valence', 'andalusia'],
    'noni': ['tokyo', 'kyoto', 'yokohama', 'kansai'],
    'any': ['moscow', 'siberia']
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places")
    for place in places:
        print(f"\t{place.title()}")
    print()
    
#6-10 Favorite numbers
favorite_numbers = {
    'miguel': [5, 1, 0, 10], 
    'frigo': [15, 8, 25, 9],
    'jaime': [8, 88, 44, 22],
    'manu': [24, 12, 48, 36],
    'adrian': [10, 98, 52, 1],
    'auron': []
}

for name, numbers in favorite_numbers.items():
    if numbers:
        print(f"{name.title()}'s favorite numbers:")
        for number in numbers:
            print(f"\t{number}")
        print()
        
#6-11 Cities
cities = {
    'tokyo': {
        'population': 14_215_906,
        'country': 'japan',
        'trivia': '“Tokyo,” means “Eastern Capital”',
    },
    'london': {
        'population': 9_002_488,
        'country': 'united kingdom',
        'trivia': 'The beloved character Winnie the Pooh' +
                ' was based on a real-life bear at London Zoo',
    },
    'sydney': {
        'population': 5_450_496,
        'country': 'australia',
        'trivia': 'Sydney was founded in the 1780s, ' + 
                'shortly after the First Fleet arrived in 1788.',
    },
    'Shenzhen': {
        'population': 10_628_900,
        'country': 'china',
        'trivia': 'Shenzhen’s rapid growth rate in the late 20th century ' + 
                'earned the nickname “Shenzhen speed” in China. ',
    },
}

for name, data in cities.items():
    print(f"{name.title()}'s info:")
    for key, value in data.items():
        print(f"\t{key.title()}: {value}")
    print()
    
#6-12 Extensions:
cities = {
    'tokyo': {
        'population': 14_215_906,
        'country': 'japan',
        'trivia': '“Tokyo,” means “Eastern Capital”',
    },
    'london': {
        'population': 9_002_488,
        'country': 'united kingdom',
        'trivia': 'The beloved character Winnie the Pooh' +
                ' was based on a real-life bear at London Zoo',
    },
    'sydney': {
        'population': 5_450_496,
        'country': 'australia',
        'trivia': 'Sydney was founded in the 1780s, ' + 
                'shortly after the First Fleet arrived in 1788.',
    },
    'Shenzhen': {
        'population': 10_628_900,
        'country': 'china',
        'trivia': 'Shenzhen’s rapid growth rate in the late 20th century ' + 
                'earned the nickname “Shenzhen speed” in China. ',
    },
}
if cities:
    for name, data in cities.items():
        if data:
            print(f"{name.title()}'s info:")
            for key, value in data.items():
                if key == 'population':
                    printable = f"\t{key.title()}: {value} habs"
                else:
                    printable = f"\t{key.title()}: {value.capitalize()}"
                print(printable)
            print()
        else:
            print(f"we don't have info of {name.title()}")
else:
    print("sorry, we haven't cities")