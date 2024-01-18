from src.hw2.figure import Figure


class Rectangle(Figure):

    def __init__(self, side_a, side_b):
        super().__init__(name="Rectangle")
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Side should be more than '0'")
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self):
        return self.side_a * self.side_b

    def get_perimeter(self):
        return (self.side_a + self.side_b) * 2

