def reverse_a_number(n: int) -> int:
    """
    Reverse the digits of the given integer.
    
    Args:
    - n (int): The input integer to be reversed.
    
    Returns:
    - int: The integer with its digits reversed.
    """
    return int(str(n)[::-1])

if __name__ == '__main__':
    print(reverse_a_number(123))
