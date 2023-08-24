def sum_of_digits(n: int) -> int:
    '''
    Gives the sum of digits of a number

    Parameters:
    n (int) -> the input number

    Returns:
    int -> sum of the digits
    '''
    total = 0
    while n > 0:
        total += n%10
        n //= 10
    return total

if __name__ == '__main__':
    print(sum_of_digits(12345))