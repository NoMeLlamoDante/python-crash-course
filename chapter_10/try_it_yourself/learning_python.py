# 10-1 Learning Python
from pathlib import Path

def read_lines(src):
    path = Path(src)
    contents = path.read_text()
    lines = contents.splitlines()
    return lines

def paragraph_text(lines): 
    text = ''
    for line in lines:
        text += line
    return text

lines = read_lines("chapter_10/try_it_yourself/learning_python.txt")

# Print as paragraph
print(paragraph_text(lines))

# Print as text
for line in lines:
    print(line)