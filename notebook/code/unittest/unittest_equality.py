
import unittest

class EqualityTest(unittest.TestCase):

    def test_Equal(self):
        self.assertEqual(1, 3)

    def test_NotEqual(self):
        self.assertNotEqual(2, 1)

if __name__ == '__main__':
    unittest.main()
