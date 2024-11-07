#9-1 Restaurant
class Restaurant:
    """Class to desribe a restaurant"""
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        description = f"The {self.name}'s is a restaurant "
        description += f"famous by our {self.cuisine_type}."
        print(description)
    
    def open_restaurant(self):
        print(f"The {self.name}'s is opened now.")

restaurant = Restaurant('Pujol', 'mexican food')
print(f"Welcome to {restaurant.name}.")
print(f"we serve {restaurant.cuisine_type}.")
restaurant.describe_restaurant()
restaurant.open_restaurant()
