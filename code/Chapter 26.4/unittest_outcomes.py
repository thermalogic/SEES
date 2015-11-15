import unittest

class OutcomesTest(unittest.TestCase):

    def test_Pass(self):
        return

    def test_Fail(self):
        self.assertFalse(True)

    def test_Error(self):
        raise RuntimeError('Test error!')

if __name__ == '__main__':
    unittest.main()
