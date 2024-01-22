import pytest

from src.hw2.triangle import Triangle


@pytest.fixture()
def init_triangle():
    return Triangle(2, 3, 1.5)


def test_triangle_area(init_triangle):
    t = init_triangle

    assert t.get_area() == 10.246950765959598, f"Area of triangle is incorrect!"


def test_triangle_perimeter(init_triangle):
    t = init_triangle
    assert t.get_perimeter() == 10, f"Perimeter of of triangle  is incorrect!"


@pytest.mark.parametrize(("side_a", "side_b", "side_c"),
                         [(-5, -3, 2), (0, 0, 0)],
                         ids=["negative", "zero_value"])
def test_triangle_negative_area(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)
