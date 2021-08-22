import unittest
from perfect_square import perfect_square
from rook_game1 import rook_distance
from converting_numbers import converting_base

class TestPerfectSquare (unittest.TestCase):
    """
    Tests the perfect_square method in perfect_square.py
    """
    def test_perfect_square(self):
        """
        Basic test of perfect_square method
        """
        print('Testing perfect_square()...')
        self.assertEqual(list(perfect_square(5)), [1,4])

        self.assertEqual(list(perfect_square(30)), [1,4,9,16,25])

        print('Finished testing perfect_square()...\n')

class TestRookGame (unittest.TestCase):
    """
    Tests the rook_distance method in rook_game1.py
    """
    def test_rook_distance(self):
        """
        Tests the rook_distance Method
        """
        print ('Testing rook_distance()....')
        directions_1 = ['up', 'up', 'down', 'down']
        steps_1 = [1,2,3,4]
        self.assertEqual(rook_distance(directions_1, steps_1), (10,4))

        directions_2 = ['down'] * 10
        steps_2 = [10] * 10
        self.assertEqual(rook_distance(directions_2, steps_2), (100,100))

        directions_3 = ['up','hello']
        steps_3 = [1,2]
        self.assertEqual(rook_distance(directions_3, steps_3), None)

        directions_4 = ['up']
        steps_4 = [1,2]
        self.assertEqual(rook_distance(directions_4, steps_4), None)
        print('Finished testing rook_distance()...\n')

class TestConvertingNumbers (unittest.TestCase):
    """
    This class tests the method converting_base() in converting_numbers.py
    """
    def test_rook_distance(self):
        """
        Tests the converting_base method
        """
        print ('Testing converting_base()....')

        self.assertEqual(converting_base(5,3), "12")
        self.assertEqual(converting_base(5,0), None)
        self.assertEqual(converting_base(100,2), "1100100")
        self.assertEqual(converting_base(100,5), "400")

        print('Finished testing converting_base()...\n')

if __name__=='__main__':
    unittest.main()
