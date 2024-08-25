def isPair(num):
    if num % 2 == 0:
        return True
    return False

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

def test_isPair():
    assert isPair(10) == True

def test_factorial():
    assert factorial(5) == 120

