#10-12 Favorite Number remembered
from pathlib import Path
import json

def read_number(src):
    """Read if a number was stored previously"""
    path = Path(src)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        # print(f"file {path} doensn't exist")
        return None
    else:
        number = json.loads(contents)
        return number

def save_number(src, number):
    """Store a data in archive"""
    path = Path(src)
    try: 
        contents = json.dumps(number)
        path.write_text(contents)
    except ValueError:
        return None
    else: 
        return True

def ask_number():
    number = input("Enter your favorite number: ")
    try:
        number = int(number)
    except ValueError:
        print(f"number invalid: {number}")
        return None
    else: 
        return number

def main():
    src = "chapter_10/try_it_yourself/favorite_number.json"
    number = read_number(src)
    if number:
        print(f"I know, your favorite number! It's {number}")
    else: 
        number = ask_number()
        save_number(src, number)

main()