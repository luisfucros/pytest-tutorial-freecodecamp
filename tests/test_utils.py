import source.utils as utils
import pytest
import time


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

@pytest.mark.slow
def test_very_slow():
    time.sleep(2)
    result = utils.divide(10, 5)

    assert result == 2

@pytest.mark.skip(reason="Feature currently broken")
def test_add_2():
    assert utils.add(1, 2) == 3

@pytest.mark.xfail(reason="Cannot divide by zero")
def test_divide_by_zero_broken():
    result = utils.divide(10, 0)