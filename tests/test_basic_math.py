import pytest
import basic_math

def test_add_nums():
    assert basic_math.add_nums(5, 5) == 10

def test_subtract_nums():
    assert basic_math.subtract_nums(10, 5) == 5
