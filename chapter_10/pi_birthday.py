from pathlib import Path

path = Path("chapter_10/pi_million_digits.txt")
containts = path.read_text()
lines = containts.splitlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form ddmmyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")