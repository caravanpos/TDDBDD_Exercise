from unittest import TestCase
import unittest
from mock_patching_side_effect import bye


class TestMockPatchingSideEffect(TestCase):

    #Firts test happy paths
    def test_side_effect_values(self):
        self.assertEqual(bye(), 'bye')

if __name__ == '__main__':
    unittest.main(verbosity=2)