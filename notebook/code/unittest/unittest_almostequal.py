import unittest

class AlmostEqualTest(unittest.TestCase):

    def test_NotAlmostEqual(self):
        self.assertNotAlmostEqual(1.11, 1.3, places=1)

    def test_AlmostEqual(self):
       # self.assertAlmostEqual(1.1, 1.3, places=0)
        self.assertAlmostEqual(0.12345678, 0.12345679) 

if __name__ == '__main__':
    unittest.main()
