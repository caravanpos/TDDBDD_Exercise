from unittest import TestCase
import unittest
from api import imdb_info


class TestApi(TestCase):

    #Firts test happy paths
    def test_good_values(self):
        """Test API where values are good"""
        self.assertEqual(imdb_info("https://www.google.com.gt"), 200)
        self.assertEqual(imdb_info("https://www.facebook.com"), 200)
        self.assertEqual(imdb_info("https://www.twitter.com"), 200)

    #Second test happy paths
    def test_second_values(self):
        """Test API where values are good"""
        self.assertEqual(imdb_info("https://www.google.com.gt"), 200)
        self.assertEqual(imdb_info("https://www.facebook.com"), 200)
        self.assertEqual(imdb_info("https://www.twitter.com"), 200)

    #Three test happy paths
    def test_three_values(self):
        """Test API where values are good"""
        self.assertEqual(imdb_info("https://www.google.com.gt"), 200)
        self.assertEqual(imdb_info("https://www.facebook.com"), 200)
        self.assertEqual(imdb_info("https://www.twitter.com"), 200)

    def test_bad_values(self):
        """Test API where values are bad"""
        self.assertEqual(imdb_info("https://www.google.com.gt/gt"), 404)
        self.assertEqual(imdb_info("https://www.facebook.com.gt/gt"), 404)


if __name__ == '__main__':
    unittest.main(verbosity=2)