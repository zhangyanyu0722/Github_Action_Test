from example import *

def test_add():
    assert add(2, 3) == 5
    assert add('boston', 'university') == 'bostonuniversity'
    
    
test_add()
