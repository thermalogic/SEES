
import unittest

class FixturesTest(unittest.TestCase):

    def setUp(self):
        print('In setUp()')
        r=1/0
        self.fixture = range(1, 10)

    def tearDown(self):
        print('In tearDown()')
        r=1/0
        del self.fixture

    def test_fixture1(self):
        print('in test1()')
        self.assertEqual(self.fixture, range(1, 10))
     
    def test_fixture2(self):
        print('in test2()')
        self.assertEqual(self.fixture, range(2, 10))

if __name__ == '__main__':
    unittest.main()