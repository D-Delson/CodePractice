def sum_of_N_natural_numbers(n: int) -> int:
    """
    Calculate the sum of the first n natural numbers.
    
    Args:
    - n (int): The number up to which the summation is required.
    
    Returns:
    - int: The sum of the first n natural numbers.
    """
    return (n * (n + 1)) // 2

if __name__ == '__main__':
    print(sum_of_N_natural_numbers(5))