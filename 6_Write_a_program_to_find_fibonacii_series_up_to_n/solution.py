def fibonacci_series(n: int) -> list[int]:
    """
    Generates the first 'n' numbers of the Fibonacci series.

    Parameters:
    - n (int): The number of terms in the Fibonacci series to generate.

    Returns:
    - list[int]: A list containing the first 'n' numbers of the Fibonacci series.
    """
    if n <= 0:
        return []

    fibo_values = [0, 1]
    for i in range(2, n):
        next_num = fibo_values[i-1] + fibo_values[i-2]
        fibo_values.append(next_num)
    
    return fibo_values

if __name__ == '__main__':
    try:
        n = int(input('Enter how many terms you want from the Fibonacci series: '))
        if n < 1:
            print('Please enter a positive number!')
        else:
            print(*fibonacci_series(n), sep=', ', end=' ')
    except ValueError:
        print("That's not a valid number!")
