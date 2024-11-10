# 10-4 Guest
from pathlib import Path

name_user = input("Please type your name: ")

path = Path("chapter_10/try_it_yourself/guest.txt")
path.write_text(name_user)