#9-4 Number Served
class Restaurant:
    """Class to desribe a restaurant"""
    def __init__(self, name, cuisine_type, number_served=0):
        """Initialize the restaurant"""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    
    def describe_restaurant(self):
        """print a simple description about our restaurant"""
        description = f"The {self.name}'s is a restaurant "
        description += f"famous by our {self.cuisine_type}."
        print(description)
    
    def open_restaurant(self):
        """A simple print to open the restaurant"""
        print(f"The {self.name}'s is opened now.")
        
    def set_number_served(self,customers):
        """set a number of customers served"""
        self.number_served=customers
    
    def increment_number_served(self, add_costumers):
        """increment the number of customers served by an number"""
        self.number_served += add_costumers
    
restaurant = Restaurant('Pujol', 'mexican food')
restaurant.describe_restaurant()
restaurant.open_restaurant()

print(f"served: {restaurant.number_served}")
restaurant.set_number_served(10)

print(f"served: {restaurant.number_served}")

restaurant.increment_number_served(50)
print(f"served: {restaurant.number_served}")