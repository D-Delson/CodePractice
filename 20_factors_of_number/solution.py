def factors(n: int) -> list:
    '''
    Gives factors of a given number

    Args:
    -n (int) -> input

    Returns:
    - list -> contains factors of a given number
    '''
    factors_list = []
    for i in range(1, n+1):
        if n % i == 0:
            factors_list.append(i)
    return factors_list

if __name__ == '__main__':
    print(*factors(6), sep = ', ', end = ' ')
