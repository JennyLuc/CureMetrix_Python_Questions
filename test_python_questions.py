import unittest
from perfect_square import perfect_square
from rook_game1 import rook_distance
from converting_numbers import converting_base
from divide import divisible_five_not_seven
from search_phrase import search_phrase_in_file
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

class TestDivide (unittest.TestCase):
    """
    This class tests the method converting_base() in divide.py
    """
    def test_divide(self):
        """
        Tests the divisibe_five_not_seven method
        """
        print ('Testing divisibe_five_not_seven()....')

        self.assertEqual(divisible_five_not_seven(-5,40),
        [-5,5,10,15,20,25,30,40])
        self.assertEqual(divisible_five_not_seven(5,0), None)

        print('Finished testing divisibe_five_not_seven()...\n')

class TestSearchPhrase (unittest.TestCase):
    """
    This class tests the method search_phrase_in_file() in search_phrase.py
    """
    def test_search_phrase_in_file(self):
        """
        Tests the divisibe_five_not_seven method
        """
        print ('Testing divisibe_five_not_seven()....')

        text_file1 = 'text_files/tester_file.txt'
        self.assertEqual(search_phrase_in_file(text_file1,'hello'), True)
        #tests if it passes substring test
        self.assertEqual(search_phrase_in_file(text_file1,'test'), False)

        text_file2 = 'text_files/tester_file2.txt'
        self.assertEqual(search_phrase_in_file(text_file2,'good'), False)

        no_file = 'text_file/no_file.txt'
        self.assertEqual(search_phrase_in_file(no_file,'good'), None)

        print('Finished testing divisibe_five_not_seven()...\n')
if __name__=='__main__':
    unittest.main()
