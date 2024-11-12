from pathlib import Path
import json

def get_stored_user(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def greet_user():
    """Greet the user by name."""
    path = Path("chapter_10/username.json")
    username = get_stored_user(path)
    if username:
        print(f"welcome back, {username}!")
    else:
        username = input("Whats your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back {username}!")

greet_user()