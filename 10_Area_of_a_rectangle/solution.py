def area_rectangle(length: float, width: float) -> float:
    '''
    Calculates and returns the area of a rectangle.

    Parameters:
    length (float): Length of the rectangle.
    width (float): Width of the rectangle.

    Returns:
    float: Area of the rectangle.
    '''
    return length * width

if __name__ == '__main__':
    try:
        length = float(input('Enter the length of the Rectangle (in cm): '))
        width = float(input('Enter the width of the Rectangle (in cm): '))
        print(f'Area of the Rectangle: {area_rectangle(length, width):.2f} cm^2')
    except ValueError:
        print("Please enter a valid number.")
