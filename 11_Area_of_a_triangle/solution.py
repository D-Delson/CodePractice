def area_triangle(base: float, height: float) -> float:
    '''
    Gives the Area of the Triangle for the given inputs

    Parameters:
    - base (float): Base size of the triangle in cm.
    - height (float): Height of the triangle in cm.

    Returns:
    float: Area of the triangle in cm^2.
    '''
    return 0.5 * base * height

if __name__ == '__main__':
    try:
        base = float(input('Enter base of the Triangle (in cm): '))
        height = float(input('Enter height of the Triangle (in cm): '))
        print(f'Area of the Triangle: {area_triangle(base, height):.2f} cm^2')
    except ValueError:
        print("Please enter a valid number.")
