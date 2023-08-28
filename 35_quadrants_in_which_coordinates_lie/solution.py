def which_coordinates(x: int, y: int) -> int:
    '''
    Gives the quadrants in whichh coordinates lie

    Args:
    - x (int) -> value of the x axis
    - y (int) -> value of the y axis

    Returns:
    - int -> coordinates value
    '''
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4

if __name__ == '__main__':
    x = int(input('Enter the value of x axis: '))
    y = int(input('Enter the value of y axis: '))
    print(which_coordinates(x, y))