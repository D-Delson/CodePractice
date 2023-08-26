def perfect_number(n: int) -> bool:
    '''
    Determine whether a number is perfect number or not

    Parameters:
    - n (int) -> input

    Returns:
    - bool -> True if perfect number else False
    '''
    total = 0
    for i in range(1, n//2+1):
        if n % i == 0:
            total += i
    return True if total == n else False
if __name__ == '__main__':
    print(perfect_number(8128))