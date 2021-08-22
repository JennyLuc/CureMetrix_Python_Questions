# CureMetrix_Python_Questions

This repository contains the code to the implementation of:
- A function that takes two integers (x and y) and returns a list of numbers
 between x and y that are divisible by 5 but not by 7.
- A function that takes two integers (x and b) as inputs and returns a string
 that represents the number x in base b.
- A generator that takes a number N and returns all perfect squares less
than N.
- A function that takes a series of movements and at the
end of the sequence of movements to print
    1. The distance traveled by the rook
    2. How far away the Rook is from its starting point

## Files

1. divide.py
2. converting_numbers.py
3. perfect_square.py
4. rook_game1.py
5. test_python_questions.py

## divide.py

This file contains the method

    divisible_five_not_seven()

Where it takes in the parameters 'lower' and 'upper' and returns a list of
 numbers between x and y that are divisible by 5 but not by 7.

### How to run the divide.py file:  

    python divide.py -l 4 -u 90

This will return a list of numbers from 4 to 90 where the numbers are
divisible by 5 but not by 7.

## perfect_square.py

This file contains the method

    perfect_square()

It takes in a parameter, N, and returns a list of numbers that are perfect squares less than N.

### How to run the perfect_square.py file:  

    python perfect_square.py -n 30

This command will return a list of perfect squares that are less than 30.

## converting_numbers.py

This file contains the method

    converting_base()

It takes in a parameter, n, a decimal number that we want to represent,
and b, the base that we want to convert n into.  

### How to run the converting_numbers.py file:  

    python converting_numbers.py -n 30 -b 2

This command will return a binary that represents 30.

## rook_game1.py

This file contains the method

    rook_distance()

It takes in two lists as its parameters:
    1. a list of directions (up, down, left, right)
    2. a list of number of steps for each direction

### How to run the rook_game1.py file:  

    python rook_game1.py -d up,down,left,right -s 2,3,6,4

This command will return a tuple where the first value represents the distance
traveled by the rook and the second value represents the distance between
the rook and the starting point.

## search_phrase.py

This file contains the method

    search_phrase_in_file()

It takes in two parameters:
    1. a text file, that it will search through
    2. a string that it will look for in the file

### How to run the rook_game1.py file:  

    python search_phrase_in_file.py -d tester_file.txt -s hello

This command will return a boolean, `True` if phrase in found in the file, and
`False` if the phrase is not found.


## test_python_questions.py
This file contains the unit test of all of the files.
To run the file:

    python test_python_questions.py
