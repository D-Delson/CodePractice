def classify_letter(letter: str) -> str:
    '''
    Classify the input letter as either a vowel or consonant.

    Parameters:
    - letter (str): A single character.

    Returns:
    - str: 'vowel', 'consonant', or 'not a letter'.
    '''
    vowels = 'aeiou'
    
    if letter.isalpha():# isalpha() returns True for alphabetic characters (a-z, A-Z)
        if letter.lower() in vowels:#lower() converts the letter to lowercase
            return 'vowel'
        return 'consonant'
    
    return 'Invalid input: not a letter'

if __name__ == '__main__':
    print(classify_letter('A'))  # Expected: vowel
    print(classify_letter('b'))  # Expected: consonant
    print(classify_letter('5'))  # Expected: Invalid input: not a letter
