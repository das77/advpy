#!/usr/bin/env python
import sys
from potus import get_info
# other imports  (standard library, standard non-library, local)
"""
Name: potus_main.py
Purpose: Exercise
Created By: David Spera
Created Date: 05/17/2023
Modified Date:
"""
# main function
def main(args):
    """
    This is the docstring for the main() function

    :param args: Command line arguments.
    :return: None
    """
    loop = True
    while loop:
        try:
            term = int(input('Enter in term number of president: '))
            loop = False
        except ValueError as err:
            print('Must be a whole number, try again')
    president = ''
    try:
        president = get_info(term)
    except Exception as err:
        print(err)
        return
    if isinstance(president, list):
        print(president[0])
    else:
        print(president)

if __name__ == '__main__':
    main(sys.argv[1:])  # Pass command line args (minus script name) to main()