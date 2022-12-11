from basic import add, diff


def test_add():
    assert add(2, 3) == 10


def test_diff():
    assert diff(5, 3) == 2
    assert diff(5, 2) == 3
    assert diff(-3, 2) == 0
