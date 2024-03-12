import logging

logging.basicConfig(level=logging.INFO)


class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius



def calculate_area(shape):
    return shape.area()



rectangle = Rectangle(5, 4)
circle = Circle(3)


logging.info("Area of Rectangle: %s", calculate_area(rectangle))
logging.info("Area of Circle: %s", calculate_area(circle))
