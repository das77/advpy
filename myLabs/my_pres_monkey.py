#!/usr/bin/env python
import sys
from president import President
# other imports  (standard library, standard non-library, local)
"""
Name: my_pres_monkey.py
Purpose: Exercise
Created By: David Spera
Created Date: 
Modified Date:
"""
# constants (AKA global variables -- keep these to a minimum)

# other functions
def full_name(self):
    """
    This is the docstring for function1().

    :return: None
    """
    return f'{self.first_name} {self.last_name}'
# main function
def main(args):
    """
    This is the docstring for the main() function

    :param args: Command line arguments.
    :return: None
    """
    setattr(President, 'get_full_name', full_name)

    don = President(45)
    print(don.get_full_name())

    joe = President(46)
    print(joe.get_full_name())

if __name__ == '__main__':
    main(sys.argv[1:])  # Pass command line args (minus script name) to main()