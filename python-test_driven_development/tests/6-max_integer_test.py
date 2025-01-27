import unittest

def max_integer(lst=[]):
    """Function that returns the largest integer from a list."""
    if not lst:
        return None
    return max(lst)


class TestMaxInteger(unittest.TestCase):

    def test_normal_case(self):
        """Test a normal list with multiple values."""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_numbers(self):
        """Test a list with negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_single_element(self):
        """Test a list with only one element."""
        self.assertEqual(max_integer([42]), 42)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer([]))

    def test_floats_and_integers(self):
        """Test a list with both float and integer values."""
        self.assertEqual(max_integer([1.5, 2, 3.5, 4]), 4)

    def test_all_equal(self):
        """Test a list where all elements are equal."""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_large_numbers(self):
        """Test a list with very large numbers."""
        self.assertEqual(max_integer([1000000, 1000001, 1000002]), 1000002)

    def test_string_in_list(self):
        """Test a list containing non-integer values."""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'three', 4])

    def test_none_in_list(self):
        """Test a list containing None values."""
        self.assertEqual(max_integer([1, None, 3]), 3)

if __name__ == '__main__':
    unittest.main()
