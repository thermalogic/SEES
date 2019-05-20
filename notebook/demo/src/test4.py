
import unittest
from region4 import *

class Region4Test (unittest.TestCase):

    def setUp(self):
        # IF97-dev,Table35 Page 34 : T(K) p(MPa)
        self.tab35=[[300, 0.353658941e-2],
                    [500, 0.263889776e1],
                    [600, 0.123443146e2]]

        # IF97-dev, Table 36 Page 36 :  p(MPa) T(K)
        self.tab36=[[0.1, 0.372755919e3],
                    [  1, 0.453035632e3],
                    [ 10, 0.584149488e3]]

    def test_pSat(self):
        places = 6
        for item in  self.tab35:
             self.assertAlmostEqual(pSat(item[0]),item[1],places)

    def test_TSat(self):
        places = 6
        for item in  self.tab36:
             self.assertAlmostEqual(TSat(item[0]),item[1],places)
     

if __name__ == '__main__':
    unittest.main()       
