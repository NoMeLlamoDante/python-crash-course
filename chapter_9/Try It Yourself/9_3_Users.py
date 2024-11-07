class User():
    """A simple class to define a user"""
    
    def __init__(self, first_name, last_name, **attribs):
        self.first_name = first_name
        self.last_name = last_name
        self.attribs = attribs
            
    
    def describe_user(self):
        full_name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"Fullname: {full_name}")
        for key, value in self.attribs.items():
            print(f"-{key}: {value}")
    
    def greet_users(self):
        print(f"Thanks {self.first_name.title()} {self.last_name.title()}")

user_0 = User(
    "dante", 'allighieri', nacionality='italian',
    job='writter')

user_1 = User(
    "beyonce", 'carter', nacionality='american',
    job='singer')

user_2 = User(
    'yato', 'calamity', job='god', tier='low')

user_0.describe_user()
user_0.greet_users()

user_1.describe_user()
user_1.greet_users()

user_2.describe_user()
user_2.greet_users()