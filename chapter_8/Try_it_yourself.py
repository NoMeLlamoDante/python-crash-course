#8-1 Message

def display_message():
    """sample display"""
    print("in this chapter you can learn functions and parameters")
    
# display_message()

#8-2 Favorite Book
def favorite_books(title):
    print(f"One of my favorite books is {title.title()}")
    
# print("the little prince")

#8-3 T-Shirt
def make_shirt(text, size):
    print(f"you order a {size} size, with the text: '{text}'")

# make_shirt("Hello world", "Large")
# make_shirt(size="Medium", text="I don't wanna be here")

#8-4 Large Shirts
def make_shirt(text="I love Python", size='Large'):
    print(f"you order a {size} size, with the text: '{text}'")

# make_shirt()
# make_shirt(size="Medium")
# make_shirt("Free PyCharm", "Small")
# make_shirt(size="XS", text="God's save to C")

#8-5 Cities
def describe_city(city, country='japan'):
    print(f'{city.title()} is in {country.title()}')

describe_city('tokyo')
describe_city('guadalajara', 'méxico')
describe_city(country='canada', city='toronto')