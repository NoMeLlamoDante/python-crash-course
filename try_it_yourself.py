#3-1 Names
friends = ['pato','mario','mayi','eva']
print(friends[0].title())
print(friends[1].title())
print(friends[2].title())
print(friends[3].title())

#3-2
print(f"thanks {friends[0].title()}, to be my friend")
print(f"thanks {friends[1].title()}, to be my friend")
print(f"thanks {friends[2].title()}, to be my friend")
print(f"thanks {friends[3].title()}, to be my friend")

#3-3
transports = ['plane', 'car', 'bus', 'motorcycle']
print(f'Gonna take her for a ride on a big jet {transports[0]}')
print(f"Sonya, the {transports[1]} was stoled when i was distracted")
print(f"i took the wrong {transports[2]} and now i'm lost ")
print(f"I would like to have an Yamaha {transports[3]}")

#3-4
guests = ['pato','mario','mayi']

print(f"Dear {guests[2].title()}, would you like to go to a dinner at home?")
print(f"Dear {guests[0].title()}, would you like to go to a dinner at home?")
print(f"Dear {guests[1].title()}, would you like to go to a dinner at home?")

#3-5
print(guests)
guests[0] = "jhony"
print(f"Dear {guests[2].title()}, would you like to go to a dinner at home?")
print(f"Dear {guests[0].title()}, would you like to go to a dinner at home?")
print(f"Dear {guests[1].title()}, would you like to go to a dinner at home?")
print(guests)
#3-6
print(guests)
print("Dear guests, we found a bigger table, we send you a new invitations")
guests.insert(0,"efren")
guests.insert(2,"miguel")
guests.append("chucho")
print(guests)
print(f"Dear {guests[0].title()}, would you like to go to a dinner at home?")
print(f"Dear {guests[1].title()}, would you like to go to a dinner at home?")
print(f"Dear {guests[2].title()}, would you like to go to a dinner at home?")
print(f"Dear {guests[3].title()}, would you like to go to a dinner at home?")
print(f"Dear {guests[4].title()}, would you like to go to a dinner at home?")
print(f"Dear {guests[5].title()}, would you like to go to a dinner at home?")

#3-7
print(guests)
print("Sorry for the trouble, but we just can invite 2 people")

unlisted_guest = guests.pop(0)
print(f"Sorry {unlisted_guest.title()}, we need to cancel your invitation")
unlisted_guest = guests.pop(1)
print(f"Sorry {unlisted_guest.title()}, we need to cancel your invitation")
unlisted_guest = guests.pop()
print(f"Sorry {unlisted_guest.title()}, we need to cancel your invitation")
unlisted_guest = guests.pop(0)
print(f"Sorry {unlisted_guest.title()}, we need to cancel your invitation")

print(f"Dear {guests[0].title()}, would you like to go to a dinner at home?")
del guests[0]
print(f"Dear {guests[0].title()}, would you like to go to a dinner at home?")
del guests[0]
print(guests)

#3-8
places_to_visit = []
places_to_visit.append("paris")
places_to_visit.append("london")
places_to_visit.append("kyoto")
places_to_visit.append("rome")
places_to_visit.append("guadalajara")
print(places_to_visit)

print(f"sorted: {sorted(places_to_visit)}")
print(places_to_visit)

places_to_visit.reverse()
print(f"reversed: {places_to_visit}")

places_to_visit.reverse()
print(places_to_visit)

# alphabetic
places_to_visit.sort()
print(places_to_visit)
# reversed alphabetic
places_to_visit.sort(reverse=True)
print(places_to_visit)

#3-9
friends = ['pato','mario','mayi','eva']
print(f"The number of ghuests in the list is: {len(guests)}")

#3-10
sad_animes = ["One piece",'clannad after story','naruto']
sad_animes[0] = '5 cm per second'
sad_animes.insert(3,'violet evergarden')
sad_animes.append('plastic memories')
print(f"list to sad anime:{sad_animes}")
print(f"wait a moment, {sad_animes[2].title()} isn't a sad anime")
sad_animes[2] = "your lie in april"
print(f"you're right, this is the list:\n{sad_animes}")
print(f"this is the alphabetic reversed list: {sorted(sad_animes, reverse = True)}")
del sad_animes[2]
sad_animes.sort()
print(f"erased the anime i've watched {sad_animes}")
next_anime = sad_animes.pop(2)
print(f"now i'm watching {next_anime}")
sad_animes.reverse()
print(f"and then i'll have {len(sad_animes)} pending animes: {sad_animes}")
print(f"the last of them: {sad_animes[3]}"),
