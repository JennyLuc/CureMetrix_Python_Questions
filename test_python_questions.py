import unittest
from perfect_square import perfect_square

class TestPerfectSquare (unittest.TestCase):
    """
    Tests the perfect_square method in perfect_square.py
    """
    def test_perfect_square_basic(self):
        """
        Basic test of perfect_square method
        """
        self.assertEqual(list(perfect_square(5)), [1,4])

        self.assertEqual(list(perfect_square(30)), [1,4,9,16,25])

        # with self.assertRaises(Exception):
        #     perfect_square(0)


if __name__=='__main__':
    unittest.main()
