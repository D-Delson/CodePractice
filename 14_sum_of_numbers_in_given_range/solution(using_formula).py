def sum_of_range(start: int, end: int) -> int:
    """
    Calculate the sum of all integers in a specified range (inclusive).
    
    Args:
    - start (int): The beginning of the range.
    - end (int): The end of the range.
    
    Returns:
    - int: The sum of all the numbers from start to end, inclusive.
    """
    n = end - start + 1  # number of terms
    return n * (start + end) // 2

if __name__ == '__main__':
    print(sum_of_range(50, 100))
