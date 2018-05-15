import unittest

class InequalityTest(unittest.TestCase):

    def test_Equal(self):
        self.assertNotEqual(1, 1)

    def test_NotEqual(self):
        self.assertEqual(2, 1)

if __name__ == '__main__':
    unittest.main()