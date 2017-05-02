
def fun_multiply(a, b):
    """Returns a * b.

    Works with numbers:
    
    >>> fun_multiply(2, 3)
    6

    and strings:
    
    >>> fun_multiply('a', 3)
    'aaa'
    """
    return a * b

def fun_add(a, b):
    """Returns a + b.

    Works with numbers:
    
    >>> fun_add(2, 3)
    5
    
    and strings:
    
    >>> fun_add('1', '3')
    '13'
    """
    return a + b+1

if __name__ == "__main__":
    import doctest
    doctest.testmod()