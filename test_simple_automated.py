import code_to_be_tested


def test_add():
    assert code_to_be_tested.add(5, 4) == 9


def test_multiply():
    assert code_to_be_tested.multiply(3, 4) == 12


def test_power():
    assert code_to_be_tested.power(2, 8) == 256
