from stats import count_words
from stats import count_characters
from stats import sort_character_count
import sys

#gets the text of a txt file as a string
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) != 2:
        #usage instructions if not expected input
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    #get book path from input variable
    book_path = sys.argv[1]

    #get the number of words in the book specified
    num_words = count_words(get_book_text(book_path)) 

    #get a dictionary consisting of each character used and their count of use in the book specified
    character_count = count_characters(get_book_text(book_path))

    #get a sorted list of dictionaries for each character in the book specified in descending order
    character_report = sort_character_count(character_count)

    #create output report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    #only print if the character is alphabetic
    for char in character_report:
        if char["char"].isalpha():
            letter = char["char"]
            count = char["num"]
            print(f"{letter}: {count}")
    
    print("============= END ===============")

main()