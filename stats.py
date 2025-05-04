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