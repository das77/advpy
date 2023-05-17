#!/usr/bin/env python
import sys
"""
Name: my_pres_by_state.py
Purpose: Exercise 1-1
Created By: David Spera
Created Date: 05/15/2023
Modified Date:
"""
# constants (AKA global variables -- keep these to a minimum)
# other functions
def import_file(filename : str):
    """
    Imports file
    :type filename: object
    :param filename: String of path to file
    :return: dict
    """
    with open(filename) as file:
        counts = {}
        for line in file:
            data = line.split(":")
            state = data[6]
            print(counts)
            if state in counts:
                counts[state] += 1
            else:
                counts[state] = 1
    return counts
# main function
def main(args):
    """
    This is the docstring for the main() function

    :param args: Command line arguments.
    :return: None
    """
    # import data file
    data = import_file('C:/Users/wasadmin/Desktop/py3interm/DATA/presidents.txt')
    # print totals sorted by state
    for state, count in sorted(data.items()):
        print(f'{state}:{count}')

if __name__ == '__main__':
    main(sys.argv[1:])  # Pass command line args (minus script name) to main()