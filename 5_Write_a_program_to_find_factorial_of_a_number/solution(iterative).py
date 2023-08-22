def factorial(n: int) -> int:
    """
    Compute the factorial of a given number.

    Parameters:
    - n (int): The input number for which factorial is to be determined.

    Returns:
    - int: Factorial of the provided number.
    """
    if n < 0:
        raise ValueError("Expected a non-negative number.")

    fact_val = 1
    for i in range(1, n + 1):
        fact_val *= i
    return fact_val

if __name__ == '__main__':
    n = int(input('Enter the number: '))
    print(factorial(n))
