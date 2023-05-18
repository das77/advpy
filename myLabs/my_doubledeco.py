#!/usr/bin/env python
import sys

# other imports  (standard library, standard non-library, local)
"""
Name: my_doubledeco.py
Purpose: Exercise 8-4
Created By: David Spera
Created Date: 05/17/2023
Modified Date:
"""
# constants (AKA global variables -- keep these to a minimum)

# other functions
def double(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper

@double
def additive(x):
    return x + 5
# main function
def main(args):
    """
    This is the docstring for the main() function
    :param args: Command line arguments.
    :return: None
    """
    print(additive(5))  # Output: 14 (2 + 5 = 7, doubled = 14)
    print(additive(9))  # Output: 30 (10 + 5 = 15, doubled = 30)

if __name__ == '__main__':
    main(sys.argv[1:])  # Pass command line args (minus script name) to main()