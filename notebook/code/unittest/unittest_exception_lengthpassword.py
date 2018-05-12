
import unittest

def raises_lengthpassword_error(password):
    if (len(password)<6):
        raise ValueError('password at least 6 characters')
  

class ExceptionTest(unittest.TestCase):

    def test_TrapLocally(self):
        try:
            raises_lengthpassword_error("123456")
        except ValueError as msg:
            pass
        else:
            self.fail('Did not see ValueError')

    def test_assertRaises(self):
        self.assertRaises(ValueError, raises_lengthpassword_error,'123456')

if __name__ == '__main__':
    unittest.main()