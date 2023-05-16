#!/usr/bin/env python
import sys
from struct import Struct
"""
Name: my_pypuzzle.py
Purpose: Exercise 4-2
Created By: David Spera
Created Date: 05/15/2023
Modified Date:
"""
# constants (AKA global variables -- keep these to a minimum)
file_path = '../DATA/puzzle.data'
# other functions
def import_file(filename : str):
    """
    :type filename: object
    :param filename: String of path to file
    :return: Tuple of integers
    """
    s = Struct('fififhHfIdfdIiIh')
    with open(filename, 'rb') as file_in:
        puzzle = file_in.read(s.size)
    return s.unpack(puzzle)

def convert_to_int(data : tuple) :
    """
    :param data: Tuple of integers
    :return: List of integers
    """
    ints = []
    for nums in data:
        ints.append(int(nums))
    return ints

def convert_to_char(data : list):
    """
    :type data: List of integers
    :return: List of strings
    """
    chars = []
    for num in data:
        chars.append(chr(num))
    return chars
# main function
def main(f_path : str, args):
    """
    Converts ASCII file into text
    :param f_path: String to path of file
    :param args: Command line arguments.
    :return: None
    """
    # import file
    values = import_file(f_path)
    # convert tuple to integers
    nums = convert_to_int(values)
    # convert ints to alpha strings
    chars = convert_to_char(nums)
    # combine strings and print result
    print(''.join(chars))

if __name__ == '__main__':
    main(file_path, sys.argv[1:])  # Pass command line args (minus script name) to main()
