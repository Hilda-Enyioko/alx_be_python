import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(-1, -1), -2)
        self.assertEqual(self.calculator.add(0, 0), 0)
        
    def test_subtraction(self):
        self.assertEqual(self.calculator.subtract(5, 3), 2)
        self.assertEqual(self.calculator.subtract(-1, 1), -2)
        self.assertEqual(self.calculator.subtract(-1, -1), 0)
        self.assertEqual(self.calculator.subtract(0, 0), 0)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(-1, 1), -1)
        self.assertEqual(self.calculator.multiply(-1, -1), 1)
        self.assertEqual(self.calculator.multiply(0, 5), 0)

    def test_division(self):
        self.assertEqual(self.calculator.divide(6, 3), 2)
        self.assertEqual(self.calculator.divide(-1, 1), -1)
        self.assertEqual(self.calculator.divide(-1, -1), 1)
        self.assertEqual(self.calculator.divide(0, 5), 0)
        self.assertEqual(self.calculator.divide(5, 0), None)
        self.assertEqual(self.calculator.divide(5, -1), -5)
        
if __name__ == '__main__':
    unittest.main()