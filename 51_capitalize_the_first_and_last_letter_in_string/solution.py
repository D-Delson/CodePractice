def capitalize_first_and_last_word(string):
    s = string.split(' ')
    words = [word.title() for word in s]
    new_words = []
    for word in words:
        l = len(word)
        new_words.append(word[0:l-1] + word[-1].capitalize())
    return ' '.join(new_words)

print(capitalize_first_and_last_word('Delson is a bad boy'))