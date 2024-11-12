#10-8 Cats and Dogs
#10-9 Silent Cats and Dogs
from pathlib import Path

prefix = "chapter_10/try_it_yourself/"
paths = ['cats.txt', 'dogs.txt']

for path in paths:
    try:
            names = Path(prefix+path)
            names = names.read_text()
    except FileNotFoundError:
        #10-9
        # print(f"the archive {path} doesn't exist")
        pass
    else:
        print(f"names of {path.replace('.txt','')}:")
        for name in names.splitlines():
            print(f"-{name}")