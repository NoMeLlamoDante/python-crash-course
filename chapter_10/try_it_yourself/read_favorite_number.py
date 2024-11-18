#10-11 Favorite number
from pathlib import Path
import json

path = Path("chapter_10/try_it_yourself/favorite_number.json")
try:
    contents = path.read_text()
except FileNotFoundError:
    print(f"file {path} doensn't exist")
else:
    number = json.loads(contents)
    print(f"I know, your favorite number! It's {number}")