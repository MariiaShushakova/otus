import pytest

from src.hw2.square import Square


@pytest.mark.parametrize(("side_a", "area"),
                         [(5, 25), (5.5, 30.25)],
                         ids=["int", "float"])
def test_square_area(side_a, area):
    s = Square(side_a)
    assert s.get_area() == area, f"Area of square with sides {s.side_a}  is incorrect!"


@pytest.mark.parametrize("side_a",
                         [(-5), 0],
                         ids=["negative", "zero_value"])
def test_square_negative_area(side_a):
    with pytest.raises(ValueError):
        Square(side_a)


def test_square_perimeter():
    s = Square(3)
    assert s.get_perimeter() == 12, f"Perimeter of square with sides {s.side_a}  is incorrect!"