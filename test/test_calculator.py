import pytest
from src import calculator

def test_add():
    assert calculator.add(1, 1) == 2
    assert calculator.add(3, 6) == 9
    assert calculator.add(134, 3426) == 3560

def test_substract():
    assert calculator.substract(1, 1) == 0
    assert calculator.substract(-234, 200) == -434
    assert calculator.substract(-140, -460) == 320
