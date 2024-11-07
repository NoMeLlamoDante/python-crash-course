#9-6 Ice Cream Stand
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

class IceCreamStand(Restaurant):
    """
    Represents aspects of a restaurant.
    specific to a Ice Cream Stand
    """
    def __init__(self, name, flavors):
        """initialize restaurant"""
        super().__init__(name,"Ice Cream")
        self.flavors = flavors
    
    def show_flavors(self):
        """Print a list of flavors"""
        print("\nThis is the list of flavors:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

IC_Stand = IceCreamStand("47", [
            'coffee', 'vanilla', 'coconut',
            'cocolate', 'strawberry', 'oreo'])

IC_Stand.show_flavors()