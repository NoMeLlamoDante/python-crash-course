from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except:
        # print(f"Sorry, the file {path} does not exist.")
        pass
    else: 
        # Count the approximate number of words in the file
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

sub = "chapter_10/"
filenames = ["alice.txt", 'siddhartha.txt', 
            'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    path = Path(sub+filename)
    count_words(path)