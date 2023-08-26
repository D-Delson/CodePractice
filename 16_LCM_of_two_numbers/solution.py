def lcm(a: int, b: int):
    '''
    Gives lcm of two numbers

    Parameters:
    - a (int) -> number 1
    - b (int) -> number 2

    Returns:
    - int -> LCM of two numbers
    '''
    if a > b:
        greater = a
    else:
        greater = b
    while True:
        if greater % a == 0 and greater % b == 0:
             return greater
        greater += 1

if __name__ == '__main__':
    print(lcm(5, 7))