import unittest

from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_area_base(self):
        self.assertAlmostEqual(3.1415, area(1), places=3)
        self.assertAlmostEqual(314.1592, area(10), places=3)
    
    def test_area_zero(self):
        self.assertEqual(0, area(0))

    def test_perimeter_base(self):
        self.assertAlmostEqual(6.2831, perimeter(1), places=3)
        self.assertAlmostEqual(62.8318, perimeter(10), places=3)
    
    def test_perimeter_zero(self):
        self.assertEqual(0, perimeter(0))
