import numpy as np
# ============================================================
# Defining your own functions here
# ============================================================

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def numpy_add(a, b):
    return np.add(a, b)

def numpy_subtract(a, b):
    return np.subtract(a, b)

# ============================================================
# Defining your own testing here
# ============================================================

def test_add():
    assert add(2, 3) == 5
    assert add('boston', 'university') == 'bostonuniversity'


def test_subtract():
    assert subtract(2, 3) == -1
    
test_add()
test_subtract()
