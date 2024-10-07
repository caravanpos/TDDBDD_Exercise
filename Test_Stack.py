from unittest import TestCase
import unittest
from stack import Stack 

class StackTestCase(TestCase):
    def setUp(self):
            """Initial Test"""
            self.stack = Stack()

    def tearDown(self):
            """Final Test"""
            self.stack = None

    def test_push(self):
           """Test Push"""
           self.stack.push(9)
           self.assertEqual(self.stack.peek(), 9)

    def test_pop(self):
           """Test Pop"""
           self.stack.push(9)
           self.assertEqual(self.stack.pop(), 9)
           self.assertTrue(self.stack.isEmpty())

if __name__ == '__main__':
    unittest.main(verbosity=2)