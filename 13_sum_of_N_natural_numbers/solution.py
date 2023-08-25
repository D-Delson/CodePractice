def sum_of_N_natural_number(n: int) -> int:
    """
    Calculate the sum of the first n natural numbers.
    
    Args:
    - n (int): The number up to which the summation is required.
    
    Returns:
    - int: The sum of the first n natural numbers.
    """
    total = 0
    for i in range(1, n+1):
        total += i
    return total

if __name__ == '__main__':
    # This will print the sum of the first 100 natural numbers
    print(sum_of_N_natural_number(100))
