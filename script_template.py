#!/usr/bin/env python
import sys

# other imports  (standard library, standard non-library, local)
"""
Name: .py
Purpose: Exercise
Created By: David Spera
Created Date: 
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
    function1()

if __name__ == '__main__':
    main(sys.argv[1:])  # Pass command line args (minus script name) to main()
