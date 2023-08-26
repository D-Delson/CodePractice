def greatest_number(a: int, b: int, c: int) -> int:
    '''
    Gives the Greatest among the given three numbers

    Args:
    - a (int) -> input 1
    - b (int) -> input 2
    - c (int) -> input 3

    Returns:
    - int -> greatest number
    '''
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b
    else:
        return c

if __name__ == '__main__':
    print(greatest_number(15, 2, 3))