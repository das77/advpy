#!/usr/bin/env python
import sys
"""
Name: my_demystify.py
Purpose: Exercise 4-1
Created By: David Spera
Created Date: 05/15/2023
Modified Date:
"""
# other imports  (standard library, standard non-library, local)

# constants (AKA global variables -- keep these to a minimum)
file_path = '../DATA/mystery'
# other functions
def import_file(filename : str):
    """
    Imports file
    :type filename: object
    :param filename: String of path to file
    :return: bytes object
    """
    with open(filename, 'rb') as file_in:
        mystery_file = file_in.read()
    return mystery_file

# main function
def main(f_path : str, args):
    """
    Converts file into ASCII art picture
    :param f_path: String of path to file
    :param args: Command line arguments.
    :return: None
    """
    # import file
    b = import_file(f_path)
    # select every third byte
    b_third = b[::3]

    # decode and print results
    print((b_third.decode()))

if __name__ == '__main__':
    main(file_path, sys.argv[1:])  # Pass command line args (minus script name) to main()
