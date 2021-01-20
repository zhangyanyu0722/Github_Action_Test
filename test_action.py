from example import * # import functions from other files

def test_add():
    assert add(2, 3) == 5
    assert add('boston', 'university') == 'bostonuniversity'


def test_subtract():
    assert subtract(2, 3) == -1
    
    
test_add()
test_subtract()
