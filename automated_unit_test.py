import unittest
import code_to_test

class SimpleMathTest(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(code_to_test.add(5, 4), 9)
    
    def test_multiply(self):
        self.assertEqual(code_to_test.multiply(3, 4), 12)

    def test_power(self):
        self.assertEqual(code_to_test.power(2, 8), 256)

unittest.main()