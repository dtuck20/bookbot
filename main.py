from stats import count_words
from stats import count_characters
from stats import sort_character_count

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()

    return file_contents

def main():
    num_words = count_words(get_book_text("books/frankenstein.txt")) 
    character_count = count_characters(get_book_text("books/frankenstein.txt"))

    #print(character_count)

    character_report = sort_character_count(character_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    #print(character_report)
    for char in character_report:
        #print(char)
        if char["char"].isalpha():
            letter = char["char"]
            count = char["num"]
            print(f"{letter}: {count}")
    
    print("============= END ===============")

main()