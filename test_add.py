import unittest

# The function we want to test
def add(a, b):
    return a + b

# Test class
class TestAddFunction(unittest.TestCase):
    
    def test_add_positive_numbers(self):
        result = add(3, 5)
        self.assertEqual(result, 8)
    
    def test_add_negative_numbers(self):
        result = add(-1, -4)
        self.assertEqual(result, -5)
    
    def test_add_mixed_numbers(self):
        result = add(2, -2)
        self.assertEqual(result, 0)

# If this file is run directly, run the tests
if __name__ == '__main__':
    unittest.main()
