def factorial(n: int) -> int:
    '''
    Gives factorial of the number

    Parameters:
    n (int) -> input

    Returns:
    int -> factorial value
    '''
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(n, 1, -1):
            fact *= i
        return fact

def strong_number(number: int) -> str:
    '''
    determine whether a number is strong number or not

    Parameters:
    - number (int) -> the number to be test

    Returns:
    - str -> 'strong number' or 'not a strong number'
    '''
    a = number
    factorial_value = []
    
    while number > 0:
        factorial_value.append(factorial(number % 10))
        number //= 10
    return 'strong number' if sum(factorial_value) == a else 'not a strong number'
        

print(strong_number(40585))
