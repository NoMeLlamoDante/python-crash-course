# 10 - 10 Common Words
from pathlib import Path

def load_book(path, error_output = True):
    """Simple way to read a text, with a cath FileNotFound Exception"""
    try:
        book = path.read_text()
    except FileNotFoundError:
        if error_output:
            print(f"the file {path} doesn't exist")
    else:
        return book

def count_word(text, word):
    """search the times a words appears in a text"""
    count = text.lower().count(word) 
    prompt = f"The word '{word}' appears {count} times"
    print(prompt)

path = Path('chapter_10/alice.txt')
words_to_count = ['alice', 'cat', 'hatter', 'queen']

alice_in_wonderland = load_book(path)
if alice_in_wonderland:
    print("In the book 'alice in wonderland': ")
    for word in words_to_count:
        count_word(alice_in_wonderland,word)