
import unittest

class OutcomesTest(unittest.TestCase):

    #   ok
    def test_Pass(self):
        return

    # FAIL
    def test_Fail(self):
        # AssertionError exception.
        self.assertFalse(True)
        
    # ERROR
    def test_Error(self):
        # raises an exception other than AssertionError
        raise RuntimeError('Test error!')

if __name__ == '__main__':
    unittest.main()