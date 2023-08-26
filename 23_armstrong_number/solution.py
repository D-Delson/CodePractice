def armstrong_number(n: int) -> bool:
    '''
    Determines whether the given number is an Armstrong number or not.

    Args:
    - n (int): Input number.

    Returns:
    - bool: True if the number is an Armstrong number, False otherwise.
    '''
    length = len(str(n))
    number = n
    total = 0

    while n > 0:
        digit = n % 10
        total += digit ** length
        n //= 10

    return total == number

if __name__ == '__main__':
    print(armstrong_number(153))
    print(armstrong_number(10))
