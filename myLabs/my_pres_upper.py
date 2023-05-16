#!/usr/bin/env python
import sys
from my_functions import convert_date_object

"""
Name: my_pres_upper.py
Purpose: Exercise 5-1
Created By: David Spera
Created Date: 05/16/2023
Modified Date:
"""
# constants (AKA global variables -- keep these to a minimum)
file_path = '../DATA/presidents.txt'
# other functions
def import_file(filename : str):
    """
    Imports file
    :type filename: object
    :param filename: String of path to file
    :return: None
    """
    # import data file
    with open(filename) as file:
        last_names = [line.split(":")[1] for line in file]
    return last_names

def main(f_path : str, args):
    """
    Imports data file and prints out list of presidents by age they took office
    :param f_path: String of path to file
    :param args: Command line arguments.
    :return: None
    """
    # import file and parse data
    data = import_file(f_path)
    names_upper = [name.upper() for name in data]
    for name in names_upper:
        print(name)

if __name__ == '__main__':
    main(file_path, sys.argv[1:])  # Pass command line args (minus script name) to main()