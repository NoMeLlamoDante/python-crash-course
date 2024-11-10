# 10-1 Learning C
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
text = paragraph_text(lines)

print(text.replace('python','C'))