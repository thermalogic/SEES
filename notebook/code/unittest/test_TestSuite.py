
import unittest

class EqualityTest(unittest.TestCase):

    def test_Equal(self):
        self.assertEqual(3, 3)

    def test_NotEqual(self):
        self.assertNotEqual(2, 3)   

class AlmostEqualTest(unittest.TestCase):

    def test_NotAlmostEqual(self):
        self.assertNotAlmostEqual(1.2, 1.1, places=1)

    def test_AlmostEqual(self):
        self.assertAlmostEqual(1.1, 1.3, places=0)

    def test_AlmostEqualWithDefault(self):
        self.assertNotAlmostEqual(1.1, 1.3)
        
def suiteEqual():
    suite = unittest.TestSuite()
    suite.addTest(EqualityTest('test_Equal'))
    suite.addTest(AlmostEqualTest('test_AlmostEqual'))
    return suite

def suiteNotEqual():
    suite = unittest.TestSuite()
    suite.addTest(EqualityTest('test_NotEqual'))
    suite.addTest(AlmostEqualTest('test_NotAlmostEqual'))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest = 'suiteNotEqual')
    #unittest.main(defaultTest = 'suiteEqual')
  
