from re import L


class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        print(self.length * self.width)

a1 = Rectangle(5,6)
a1.area()