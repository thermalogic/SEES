
import unittest

def raises_error(*args, **kwds):
    print(args, kwds) # *args: tuple; **kwds: dict
    if len(args)<2:
        raise ValueError('Invalid value: ' + str(args) + str(kwds))
    else:
        pass

class ExceptionTest(unittest.TestCase):

    def test_TrapLocally(self):
        try:
            raises_error('a', b='c') # ('a',), 'b':'c'}
            #raises_error('a','b', b='c',d='e') 
        except ValueError:
            pass
        else:
            self.fail('Did not see ValueError')

    def test_assertRaises(self):
        self.assertRaises(ValueError, raises_error, 'a', b='c')

if __name__ == '__main__':
    unittest.main()