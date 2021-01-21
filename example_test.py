from example import * # import functions from other files

def test_add():
    assert add(2, 3) == 5
    assert add('boston', 'university') == 'bostonuniversity'
    assert numpy_add(1, 5) == 6


def test_subtract():
    assert subtract(2, 3) == -1
    assert numpy_subtract(0, 1) == -1
