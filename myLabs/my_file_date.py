#!/usr/bin/env python
import sys
import os
# other imports  (standard library, standard non-library, local)
from DateTime import DateTime

"""
Name: my_file_date.py
Purpose: Exercise 3-1
Created By: David Spera
Created Date: 05/17/2023
Modified Date:
"""
# constants (AKA global variables -- keep these to a minimum)

# other functions
def function1():
    """
    This is the docstring for function1().

    :return: None
    """
    pass
# main function
def main(args):
    """
    This is the docstring for the main() function

    :param args: Command line arguments.
    :return: None
    """
    filename = args
    for file in filename:
        mod_time = os.path.getmtime(filename)
        file_date = DateTime.fromtimestamp(mod_time)
        print(f'{file}, {file_date.strftime("%b %d, %Y")}')

    function1()

if __name__ == '__main__':
    main(sys.argv[1:])  # Pass command line args (minus script name) to main()