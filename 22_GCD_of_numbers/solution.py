def GCD(a: int, b: int) -> int:
    '''
    Gives the Greates common divisor of a number

    Parameters:
    - a (int) -> input number 1
    - b (int) -> input number 2

    Returns:
    int -> Greatest common divisor of a given numbers
    '''
    if a > b:
        greater = a
    else:
        greater = b
    for i in range(greater, 1, -1):
        if a % i == 0 and b % i == 0:
            return i
if __name__ == '__main__':
    print(GCD(12, 60))