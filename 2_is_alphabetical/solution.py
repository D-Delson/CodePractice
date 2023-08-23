def is_alphabetical(letter: str) -> str:
    '''
    Check whether the given string is alphabetical or not.

    Parameters:
    letter (str): Input string to check.

    Returns:
    str: 'Given string is alphabetical' or 'Not alphabetical'.
    '''
    return 'Given string is alphabetical' if letter.isalpha() else 'Not alphabetical'

if __name__ == '__main__':
    print(is_alphabetical('A'))      # Expected: Given string is alphabetical
    print(is_alphabetical('h'))      # Expected: Given string is alphabetical
    print(is_alphabetical('7'))      # Expected: Not alphabetical
    print(is_alphabetical('\\'))     # Expected: Not alphabetical
    print(is_alphabetical('@'))      # Expected: Not alphabetical
    print(is_alphabetical('Abc15'))  # Expected: Not alphabetical
    print(is_alphabetical('Abcd'))   # Expected: Given string is alphabetical
