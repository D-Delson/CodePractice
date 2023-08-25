def reverse_integer(n: int) -> list:
    """
    Reverse the digits of the given integer.
    
    Args:
    - n (int): The input integer to be reversed.
    
    Returns:
    - list: The list with its digits reversed.
    """
    
    reversed_digits = []
    
    while n > 0:
        last_digit = n % 10
        reversed_digits.append(last_digit)
        n //= 10
        
    # Convert list of digits back to integer
    return reversed_digits

if __name__ == '__main__':
    print(*reverse_integer(123), sep ='')
