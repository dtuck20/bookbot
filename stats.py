def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

def count_characters(text):
    text = text.lower()
    words = text.split()

    count = {}
    for word in words:
        for letter in word:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1
    return count

def sort_on(dict):
    return dict["num"]


def sort_character_count(character_counts):
    character_dictionaries = []


    for character in character_counts:
        char_count = character_counts[character]
        #print(character)
        character_dictionary = {"char": character,
                                "num": char_count}
        character_dictionaries.append(character_dictionary)
        character_dictionaries.sort(reverse=True, key=sort_on)
    return character_dictionaries
