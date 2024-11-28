import unittest

from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_area_base(self):
        self.assertEqual(1, area(1))
        self.assertEqual(25, area(5))

    def test_area_zero(self):
        self.assertEqual(0, area(0))

    def test_perimeter_base(self):
        self.assertEqual(4, perimeter(1))
        self.assertEqual(40, perimeter(10))
    
    def test_perimeter_zero(self):
        self.assertEqual(0, perimeter(0))
