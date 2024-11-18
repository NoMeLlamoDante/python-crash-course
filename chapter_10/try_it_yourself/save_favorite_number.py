#10-11 Favorite Number
from pathlib import Path
import json

number = input("Enter your favorite number: ")
path = Path("chapter_10/try_it_yourself/favorite_number.json")
try: 
    number = int(number)
except ValueError:
    print(f'number invalid: {number}')
else: 
    contents = json.dumps(number)
    path.write_text(contents)
    print("saved")