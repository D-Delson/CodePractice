def check_odd_even(n: int) -> str:
    """
    Determines if a number is Odd or Even.

    Parameters:
    - n (int): The input number.

    Returns:
    - str: 'Odd' or 'Even' based on the number's parity.
    """
    return 'Even' if n % 2 == 0 else 'Odd'

if __name__ == '__main__':
    assert check_odd_even(-6) == 'Even'
    assert check_odd_even(0) == 'Even'
    assert check_odd_even(4) == 'Even'
    assert check_odd_even(3) == 'Odd'
    assert check_odd_even(-3) == 'Odd'
    
    print('All tests passed')
