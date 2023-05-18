#!/usr/bin/env python
import sys
from president import President

# other imports  (standard library, standard non-library, local)
"""
Name: my_pres_attr.py
Purpose: Exercise
Created By: David Spera
Created Date: 
Modified Date:
"""
# constants (AKA global variables -- keep these to a minimum)

# main function
def main(args):
    """
    This is the docstring for the main() function

    :param args: Command line arguments.
    :return: None
    """
    for term in 10, 11, 12:
        p = President(term)

        last_name = getattr(p, 'last_name')
        first_name = getattr(p, 'first_name')
        party = getattr(p, 'party')
        print(f'{first_name} {last_name} was a {party}' )

if __name__ == '__main__':
    main(sys.argv[1:])  # Pass command line args (minus script name) to main()