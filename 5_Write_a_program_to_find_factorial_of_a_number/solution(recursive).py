def factorial(n:int) -> int:
    """
    Compute the factorial of a given number.

    Parameters:
    - n (int): The input number for which factorial is to be determined.

    Returns:
    - int: Factorial of the provided number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == '__main__':
    print(factorial(5))