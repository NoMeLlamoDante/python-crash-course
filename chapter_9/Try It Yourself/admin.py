from users import User
class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges
    
    def show_privileges(self):
        """List all the privileges of the admin"""
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege.title()}")    

class Admin(User):
    """A class of user defined as administrator"""
    
    def __init__(self, first_name, last_name, privileges=None):
        """Initialize user, and add privileges"""
        super().__init__(first_name,last_name)
        self.privileges = Privileges(privileges)