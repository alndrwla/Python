from algorithms import fibonacci, palindrome, factorial

def test_bfibonaci_five():
    assert fibonacci(5) == 5

def test_palindrome_anita():
    assert palindrome("Anita lava la tina")


def test_factorial_five():
    assert factorial(5)==120

#pytest test.py