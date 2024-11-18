#10-14 Verify User
from pathlib import Path
import json

def get_stored_user(path):
    """Get stored user if available."""
    if path.exists():
        contents = path.read_text()
        user = json.loads(contents)
        return user
    else:
        return None

def store_user(path, user):
    """Save user in an archive"""
    try:
        containts = json.dumps(user)
        path.write_text(containts)
    except :
        return None
    else:
        return True
    
def get_new_user(path):
    """Prompt for a new user."""
    name = input("Whats your name? ")
    last_name = input("Whats your last name? ")
    
    while True:
        age = input("Whats your age? ")
        try:
            age = int(age)
            break
        except: 
            print(f"invalid data {age}")
            continue
    
    user = {}
    user['name'] = name
    user['last_name'] = last_name
    user['age'] = age
    
    contents = json.dumps(user)
    path.write_text(contents)
    return user

def greet_user():
    """Greet the user by name."""
    path = Path("chapter_10/try_it_yourself/user.json")
    user = get_stored_user(path)
    if user:
        confirm = input(f"Are you {user['name']}? [Y/N]")
        if confirm.lower() == 'y':
            print(f"welcome back, {user['name']} {user['last_name']}!")
            print(f"You are {user['age']} years old")
        else: 
            user = get_new_user(path)
            print(f"We'll remember you when you come back {user['name']}!")
    else:
        user = get_new_user(path)
        print(f"We'll remember you when you come back {user['name']}!")

greet_user()