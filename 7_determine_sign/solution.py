def determine_sign(n: int) -> str:
    """
    Determines the sign of the given number.

    Parameters:
    n (int): The input number.

    Returns:
    str: 'Positive', 'Negative', or 'Zero' based on the sign of the number.
    """
    if n > 0:
        return 'Positive'
    elif n == 0:
        return 'Zero'
    else:
        return 'Negative'

if __name__ == '__main__':
    assert determine_sign(-7) == 'Negative'
    assert determine_sign(7) == 'Positive'
    assert determine_sign(0) == 'Zero'
    print("All tests passed!")
