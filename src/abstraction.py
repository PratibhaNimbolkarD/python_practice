import logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO , format= '%(message)s')


class Shape(ABC):
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return 4 * self.side_length


square = Square(int(input("Enter the number : ")))
logging.info(f"Area of Square: {square.area()}")
logging.info(f"Perimeter of Square: {square.perimeter()}")
