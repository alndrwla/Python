""" 
>>> recursive = Recursive()
>>> recursive.factorial(5)
120
"""
def fibonacci(number):
    if number == 0: return 0
    elif number == 1: return 1
    else: return fibonacci(number-1) + fibonacci(number-2)

def palindrome(sentence):
    """Return int if param is palindrome
    if diferent case return false
    sentence ---String or int
    
    >>> palindrome("anita lava la tina")
    True
    >>> palindrome("NO")
    False
    """
    sentence = str(sentence).lower().replace(" ","")
    return sentence == sentence[::-1]

class Recursive():
    def factorial(self, number):
        if number == 0: return 1
        else: return number * self.factorial(number - 1)

if __name__=='__main__':
    import doctest
    doctest.testmod()
    doctest.testfile('test.txt')

#python -m doctest -v algorithms.py
