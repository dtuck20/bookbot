from stats import count_words
from stats import count_characters

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()

    return file_contents

def main():
    num_words = count_words(get_book_text("books/frankenstein.txt")) 
    print(f"{num_words} words found in the document")

    character_count = count_characters(get_book_text("books/frankenstein.txt"))

    print(character_count)

main()