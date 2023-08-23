def sum_of_digits(number: int) -> int:
    """
    Compute the sum of individual digits of a given non-negative integer.

    Parameters:
    - number (int): A non-negative integer.

    Returns:
    - int: The sum of individual digits of the number.

    Raises:
    - ValueError: If the provided number is negative.
    """
    return sum(int(digit) for digit in str(number))

if __name__ == '__main__':
    try:
        number = int(input('Enter a non-negative integer: '))
        if number < 0:
            raise ValueError("Please enter a non-negative integer.")
        print(sum_of_digits(number))
    except ValueError as e:
        print(e)
