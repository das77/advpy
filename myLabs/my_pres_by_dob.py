#!/usr/bin/env python
import sys
from my_functions import convert_date_object

"""
Name: my_pres_dob.py
Purpose: Exercise 5-2
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
        all_pres = [(f'{line.split(":")[2]} {line.split(":")[1]}',
                    convert_date_object(line.split(":")[3]),
                    line.split(":")[9].strip('\n'))
                    for line in file]
    return all_pres

def records(name, dob, aff):
    print(name, dob.strftime("%m/%d/%Y"), aff)


def main(f_path : str, args):
    """
    Imports data file and prints out list of presidents by age they took office
    :param f_path: String of path to file
    :param args: Command line arguments.
    :return: None
    """
    # import file and parse data
    data = import_file(f_path)

    for item in sorted(data, key=lambda x: x[1]):
        records(*item)

if __name__ == '__main__':
    main(file_path, sys.argv[1:])  # Pass command line args (minus script name) to main()