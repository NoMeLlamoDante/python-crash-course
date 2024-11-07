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

Restaurant_1 = Restaurant('Burguer King', 'american food')
Restaurant_2 = Restaurant('Storia', 'italian food')
Restaurant_3 = Restaurant('Panda Express', 'chinese food')

Restaurant_1.describe_restaurant()
Restaurant_2.describe_restaurant()
Restaurant_3.describe_restaurant()