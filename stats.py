#function that counts the number of words in the input string
def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

#function that returns a dictionary containing each character used in the input string and how many times it is used
def count_characters(text):
    #set all lowercase in order to get one result per letter
    text = text.lower()
    words = text.split()

    count = {}
    #for each word, check if each letter is already in the count dictionary. 
    #if existing in dictionary, add to the count
    #if not in dictionary, add to the dictionary with the count of 1
    for word in words:
        for letter in word:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1
    return count

#sorting key for the list of dictionaries
def sort_on(dict):
    return dict["num"]

#returns a sorted list of dictionaries for each character used in the input string. Sorted in descending order by the number of times the character is used
def sort_character_count(character_counts):
    character_dictionaries = []

    #for each character in the input dictionary, create it's own dictionary containing the character and the count of use
    for character in character_counts:
        char_count = character_counts[character]
        character_dictionary = {"char": character,
                                "num": char_count}
        #add each new dictionary to the list of dictionaries called character_dictionaries
        character_dictionaries.append(character_dictionary)
        #sort the list of dictionaries in descending order
        character_dictionaries.sort(reverse=True, key=sort_on)
    return character_dictionaries
