from src import calculator


def test_add():
    assert calculator.add(1, 1) == 2
    assert calculator.add(3, 6) == 9
    assert calculator.add(134, 3426) == 3560


def test_substract():
    assert calculator.substract(1, 1) == 0
    assert calculator.substract(-234, 200) == -434
    assert calculator.substract(-140, -460) == 320


def test_multiply():
    assert calculator.multiply(1, 1) == 1
    assert calculator.multiply(5, 2) == 10
    assert calculator.multiply(124124, 0) == 0


def test_divide():
    assert calculator.divide(2, 1) == 2
    assert calculator.divide(10, 2) == 5
    assert calculator.divide(100, 25) == 4
