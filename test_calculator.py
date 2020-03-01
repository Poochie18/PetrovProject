from unittest import TestCase
from calc import Calculator


class TestCalculator(TestCase):
    def init(self):
        a = Calculator(4, -8)
        self.assertEqual(Calculator(a.first), 3)
        self.assertEqual(Calculator(a.second), -8)
    def test_div(self):
        b = Calculator(4, -8)
        c = Calculator(2, 2)
        self.assertEqual(Calculator.div(b.first, b.second), -0.5)
        self.assertEqual(Calculator.div(c.first, c.second), 1)

    def test_add(self):
        a = Calculator(2,7)
        b = Calculator(0, 0)
        c = Calculator(1,4)
        self.assertEqual(Calculator.add(a, b), False)
        self.assertEqual(Calculator.add(a, c), 0.63571)

    def test_simply(self):
        self.assertEqual(Calculator.simply(8,-3), True)