import pytest



@pytest.fixture()
def init_rectangle():
    def _wrapper(value: str):
        if value == "int":
            return 3, 5, 15
        elif value == "float":
            return 3.5, 5.5, 19.25

    return _wrapper
