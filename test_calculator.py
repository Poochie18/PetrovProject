from unittest import TestCase
from calc import Calculator


class TestCalculator(TestCase):

    def test_div(self):
        a = Calculator(2,-4)
        b = Calculator(4,-4)
        c = Calculator(1, 1000000000)
        self.assertEqual(Calculator.div(b.first,b.second), -1)
        self.assertEqual(Calculator.div(b.first, b.second), -1.0)
        self.assertEqual(Calculator.div(b.first, b.second), -1.0000000000000001)
        self.assertEqual(Calculator.div(c.first, c.second), 0.000000001)
        self.assertEqual(Calculator.add(a,b),-1.5)
        self.assertEqual(Calculator.simply(a.second, b.second), 4)

    def test_simply(self):
        print('Hello')
        a = Calculator(2,-3)
        self.assertEqual(Calculator.simply(a.first,a.second),24)