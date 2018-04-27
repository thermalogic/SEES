
import unittest

class FailureMessageTest(unittest.TestCase):

    def test_Fail(self):
        self.assertFalse(True,'failure message goes here')

if __name__ == '__main__':
    unittest.main()