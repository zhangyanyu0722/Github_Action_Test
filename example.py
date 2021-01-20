# ============================================================
# Defining your own functions here
# ============================================================
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# ============================================================
# Defining your own testing here
# ============================================================
def test_add():
    assert add(2, 3) == 5
    assert add('boston', 'university') == 'bostonuniversity'


def test_subtract():
    assert subtract(2, 3) == -1
