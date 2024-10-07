from unittest import TestCase
import unittest
from triangle import area_of_a_triangle


class TestAreaOfTriangle(TestCase):

    #Firts test happy paths
    def test_good_values(self):
        """Test areas where values are good"""
        self.assertAlmostEqual(area_of_a_triangle(3.4556, 8.3567), 14.43870626)
        self.assertEqual(area_of_a_triangle(2 ,5), 5.0)
        self.assertEqual(area_of_a_triangle(0, 5), 0.0)
    
    #print(area_of_a_triangle(2, 5))

    #Second test sad paths
    def test_bad_values(self):
        """Test that ValueError is raised for bad values"""
        self.assertRaises(ValueError, area_of_a_triangle, -2, 5)
        self.assertRaises(ValueError, area_of_a_triangle, 2, -5)

    def test_bad_types(self):
        """Test that TypeError is raised for bad types"""
        self.assertRaises(TypeError, area_of_a_triangle, True, 5)
        self.assertRaises(TypeError, area_of_a_triangle, 2, True)
        self.assertRaises(TypeError, area_of_a_triangle, "base", 5)
        self.assertRaises(TypeError, area_of_a_triangle, 2, "height")

    #def test_push(self):
     #   raise Exception("Not implemented")

if __name__ == '__main__':
    unittest.main(verbosity=2)