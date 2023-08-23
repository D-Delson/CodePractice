import math

def area_circle(radius: float) -> float:
    """
    Computes the area of a circle for a given radius.

    Parameters:
    - radius (float): Radius of the circle.

    Returns:
    - float: Area of the circle.

    Raises:
    - ValueError: If the provided radius is negative.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius * radius

if __name__ == '__main__':
    assert round(area_circle(7), 2) == 153.94
    assert round(area_circle(0), 2) == 0.00
    assert round(area_circle(1), 2) == 3.14
    assert round(area_circle(5.5), 2) == 95.03

    print('All tests Passed')
