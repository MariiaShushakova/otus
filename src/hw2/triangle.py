from src.hw2.figure import Figure


class Triangle(Figure):

    def __init__(self, side_a, side_b, side_c):
        super().__init__(name="Triangle")

        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Side should be more than '0'")

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError("The sum of any two sides should be greater than third side.")

    def get_perimeter(self):
        return (self.side_a + self.side_b) * 2

    def get_area(self):
        #semi_perimeter
        s = self.get_perimeter() / 2

        return (s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)) ** 0.5
