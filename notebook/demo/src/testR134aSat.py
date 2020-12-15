
import unittest
from  R134aSat import *

class  R134aSatest (unittest.TestCase):

    def setUp(self):
        #  t, p
        self.table=[[-8, 0.21704],
                    [0, 0.29282],
                    [8,0.38756]
                   ]
                    
      
    def test_pSat(self):
        places = 3
        for item in  self.table:
             self.assertAlmostEqual(pSat(item[0]),item[1],places)

if __name__ == '__main__':
    unittest.main()       
