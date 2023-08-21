def count_digits(number: int) -> int:
    '''
    Return the number of digits in the given number.

    Parameters:
    - number (int): The integer whose digits are to be counted.

    Returns:
    - int: Number of digits in the given number.
    '''
    return len(str(abs(number)))

if __name__ == '__main__':
    print(count_digits(10000))  # Expected: 5
