#8-1 Message

def display_message():
    """sample display"""
    print("in this chapter you can learn functions and parameters")
    
# display_message()

#8-2 Favorite Book
def favorite_books(title):
    """Display a book as parameter"""
    print(f"One of my favorite books is {title.title()}")
    
# print("the little prince")

#8-3 T-Shirt
def make_shirt(text, size):
    """display a text with 2 parameters"""
    print(f"you order a {size} size, with the text: '{text}'")

# make_shirt("Hello world", "Large")
# make_shirt(size="Medium", text="I don't wanna be here")

#8-4 Large Shirts
def make_shirt(text="I love Python", size='Large'):
    """Display a text using 2 keyword arguments with default values"""
    print(f"you order a {size} size, with the text: '{text}'")

# make_shirt()
# make_shirt(size="Medium")
# make_shirt("Free PyCharm", "Small")
# make_shirt(size="XS", text="God's save to C")

#8-5 Cities
def describe_city(city, country='japan'):
    """Display a phrase using a positional parameter and a keyword argument"""
    print(f'{city.title()} is in {country.title()}')

# describe_city('tokyo')
# describe_city('guadalajara', 'méxico')
# describe_city(country='canada', city='toronto')

#8-6 City names
def city_country(city, country):
    return f"{city.title()}, {country.title()}"

# print(city_country('zaragoza', 'spain'))
# print(city_country('london', 'united kingdom'))
# print(city_country('lima', 'peru'))

#8-7 Album
def make_album(artist, title, songs=None):
    return {
        'album artist': artist, 
        'album title':title, 
        'songs': songs
    }

# print(make_album('michael jackson', 'thriller',7))
# print(make_album('ed sheeran', '+'))
# print(make_album('the beetles', "Sgt. Pepper's Lonely Hearts Club Band"))

#8-8 User Albums


while True:
    print("Let's add album info:")
    print("(enter 'q' to quit)")
    
    artist = input("Enter artist album: ")
    if artist == 'q':
        break
    
    title = input("Enter album title: ")
    if title == 'q':
        break
    
    no_songs = input("Enter number of songs: ")
    if no_songs == 'q':
        break
    if no_songs == "":
        no_songs = 0
    else: 
        no_songs = int(no_songs)
    
    if artist and title and no_songs > 0:
        album = make_album(artist, title, no_songs)
    elif artist and title:  
        album = make_album(artist, title)
    
    print(album)