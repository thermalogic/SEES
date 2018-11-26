import unittest
import seuif97

class Region1Test (unittest.TestCase):

    def setUp(self):
        self.T0=273.15

        # IF97-dev,Table 5 Page 9 : p,t(K),h,s
        self.tab5=[ [ 3, 300, 0.115331273e3, 0.392294792 ],
                     [80, 300, 0.184142828e3, 0.368563852 ],
                     [ 3, 500, 0.975542239e3, 0.258041912e1]]

    def testSpecificEnthalpyPT(self):
        #places = 8
        places = 6
        for item in  self.tab5:
             self.assertAlmostEqual(seuif97.pt(item[0], item[1]-self.T0,4),item[2],places)

    def testSpecificEntropyPT(self):
        places = 8
        for item in  self.tab5:
             self.assertAlmostEqual(seuif97.pt(item[0], item[1]-self.T0,5),item[3],places)

if __name__ == '__main__':
    unittest.main()            
