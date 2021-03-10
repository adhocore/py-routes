import os
import unittest


class TestCase(unittest.TestCase):
    TEST_CSV = __file__ + '.csv'

    def setUp(self):
        with open(self.TEST_CSV, 'w+') as file:
            csv = '"A", B,5\nB,"C",5\nC,D ,7\nA,D,"15"\n E,\tF,5\nF,G, 5\nG,H,10 \n'
            file.write(csv + 'H,  I,10\nI,\tJ,5\nG,J,\t20\n\n,X,Y\n,X,\nZ')

    def tearDown(self):
        os.remove(self.TEST_CSV)
