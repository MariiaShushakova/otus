from src.hw2.figure import Figure
import math as m


class Circle(Figure):
    def __init__(self, radius):
        super().__init__(name="Circle")
        if radius <= 0:
            raise ValueError("Side should be more than '0'")
        self.radius = radius

    def get_area(self):
        return m.pi * (self.radius ** 2)

    def get_perimeter(self):
        return 2 * m.pi * self.radius

