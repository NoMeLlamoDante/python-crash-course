class User():
    """A simple class to define a user"""
    
    def __init__(self, first_name, last_name, login_attemps=0, **attribs):
        """initialize user class"""
        self.first_name = first_name
        self.last_name = last_name
        self.attribs = attribs
        self.login_attemps = login_attemps
    
    def describe_user(self):
        """basic description of user"""
        full_name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"Fullname: {full_name}")
        for key, value in self.attribs.items():
            print(f"-{key}: {value}")
    
    def greet_users(self):
        """a simple text to greed user"""
        print(f"Thanks {self.first_name.title()} {self.last_name.title()}")
    
    def increment_login_attempts(self):
        """increment login attempts by 1"""
        self.login_attemps += 1

    def reset_login_attempts(self):
        """set login attempts to 0"""
        self.login_attemps = 0

user_0 = User('yato', 'calamity', job='god')

user_0.describe_user()
print(f"login attempts: {user_0.login_attemps}")

user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
print(f"login attempts: {user_0.login_attemps}")

user_0.reset_login_attempts()
print(f"login attempts: {user_0.login_attemps}")