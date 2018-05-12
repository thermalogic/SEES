
import unittest

class Exception_Error_Test(unittest.TestCase):

    # ERROR
    def test_Error(self):
        # raises an exception other than AssertionError
        raise RuntimeError('Test error!')
        assertTrue(True)

if __name__ == '__main__':
    unittest.main()