import pytest

from src.hw2.circle import Circle


@pytest.fixture()
def init_circle():
    return Circle(2)


def test_circle_area(init_circle):
    c = init_circle

    assert c.get_area() == 12.566370614359172, f"Area of circle is incorrect!"


def test_circle_perimeter(init_circle):
    c = init_circle
    assert c.get_perimeter() == 12.566370614359172, f"Perimeter of circle is incorrect!"


@pytest.mark.parametrize("radius",
                         [(-5), 0],
                         ids=["negative", "zero_value"])
def test_circle_negative_area(radius):
    with pytest.raises(ValueError):
        Circle(radius)
