#10-5 Guest Book
from pathlib import Path

path = Path("chapter_10/try_it_yourself/guest_book.txt")
names = ''

while True:
    name = input("Please type your name: (type 'q' to quit): ")
    if name == 'q':
        break
    else: 
        names += f"{name}\n"

path.write_text(names)