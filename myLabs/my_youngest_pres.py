#!/usr/bin/env python
import sys
from my_functions import convert_date_object

"""
Name: my_youngest_pres.py
Purpose: Exercise 3-4
Created By: David Spera
Created Date: 05/15/2023
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
        all_pres = []
        for line in file:
            # parse file
            data = line.split(":")
            # get date born
            born = convert_date_object(data[3])
            # get date started office
            office_date = convert_date_object(data[7])
            # calc age
            age = office_date - born
            age_calc = int(age.days) / 365
            # get name and combine
            name = f'{data[2]} {data[1]}'
            all_pres.append((int(age_calc), name))
    return all_pres

def main(f_path : str, args):
    """
    Imports data file and prints out list of presidents by age they took office
    :param f_path: String of path to file
    :param args: Command line arguments.
    :return: None
    """
    # import file and parse data
    data = import_file(f_path)
    # print names sorted by age
    for age, name in sorted(data):
        print(f"President {name} was {age} on the date they took office")

if __name__ == '__main__':
    main(file_path, sys.argv[1:])  # Pass command line args (minus script name) to main()