from datetime import datetime

import pytest

from src.hw2.rectangle import Rectangle


@pytest.mark.parametrize("value", ["int", "float"], ids=["int", "float"])
def test_rectangle_area(init_rectangle, value):
    a, b, area = init_rectangle(value=value)
    r = Rectangle(a, b)
    assert r.get_area() == area, f"Area of rectangle with sides {r.side_a} & {r.side_b} is incorrect!"


@pytest.mark.parametrize(("side_a", "side_b"),
                         [(-3, -5), (-3, 5), (0, 5)],
                         ids=["both_negative", "one_negative", "zero_value"])
@pytest.mark.skipif(condition=datetime.now().hour == 2, reason="Test")  # just for study purposes
@pytest.mark.fun  # just for study purposes
def test_rectangle_negative_area(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


def test_rectangle_perimeter():
    r = Rectangle(3,5)
    assert r.get_perimeter() == 16, f"Perimeter of rectangle with sides {r.side_a} & {r.side_b} is incorrect!"
