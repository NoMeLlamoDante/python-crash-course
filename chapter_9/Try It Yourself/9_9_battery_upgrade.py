#9-9 Battery Upgrade
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return to a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This has has: {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: 
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        """put the gas tank on full"""
        print("gas thank full")

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This har has a {self.battery_size}-kWh battery")
    
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        
        print(F"This car can go about {range} miles on a full charge")
    
    def upgrade_batery(self):
        """put a battery of 65 kWh, if the car desn't have it"""
        if self.battery_size < 65:
            print("Battery upgraded")
            self.battery_size = 65
        else:
            print(f"you already have a {self.battery_size} kWh battery")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialize attribute of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
        
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")

model_s = ElectricCar("Tesla", 'S', "2024")
model_s.battery.describe_battery()
model_s.battery.get_range()

model_s.battery.upgrade_batery()
model_s.battery.describe_battery()
model_s.battery.get_range()