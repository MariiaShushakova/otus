from abc import ABC, abstractmethod


class Figure(ABC):

    def __init__(self, name: str):
        self.name = name

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Instance should be a figure")
        return self.get_area() + other_figure.get_area()

    @abstractmethod
    def get_area(self):
        pass
