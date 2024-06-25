import source.utils as utils
import pytest


def test_add():
    result = utils.add(1, 4)

    assert result == 5

def test_add_strings():
    result = utils.add("I like ", "swimming")

    assert result == "I like swimming"

def test_divide():
    result = utils.divide(10, 5)

    assert result == 2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        result = utils.divide(10, 0)
