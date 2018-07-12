import unittest
import sys
sys.path.append('../')
from calculator import Calculator

def setUpModule():
    print('set up module')

def tearDownModule():
    print('tear down module')

class TestCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('Set up class')
        # Create an instance of the calculator that can be used in all tests
        self.calc = Calculator()

    @classmethod
    def tearDownClass(self):
        print('Tear down class')

    def test_add(self):
        self.assertEqual(self.calc.add(2, 7), 9)

    # Write test methods for subtract, multiply, and divide

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(self.calc.divide(22, 2), 11)

if __name__ == '__main__':
    unittest.main()