#!/usr/bin/env python
import sys
from my_functions import convert_date_object

"""
Name: my_pres_dates_amb.py
Purpose: Exercise 1-2
Created By: David Spera
Created Date: 05/15/2023
Modified Date:
"""
# constants (AKA global variables -- keep these to a minimum)
file_path = '../DATA/presidents.txt'
# other functions
def import_file(filename : str):
    """
    Imports file and parses data
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
            born = data[3]
            # get date died
            died = '***' if data[4] == 'NONE' else data[4]
            # get name and combine
            name = f'{data[2]} {data[1]}'
            all_pres.append({"name": name,"dob": born,"dec": died})
    return all_pres

def main(f_path : str, args):
    """
    Imports data file and prints out list of presidents by age they took office
    :param f_path: String of path to file
    :param args: Command line arguments.
    :return: None
    """
    # ask for name
    name = input('Enter in name: ')
    # import file and parse data
    data = import_file(f_path)
    if all_matches := [x for x in data if name.upper() in x['name'].upper()]:
        for data in all_matches:
            print(f'{data["name"]}, Born: {data["dob"]}, Died: {data["dec"]}')
    else:
        print('No matching names found')

if __name__ == '__main__':
    main(file_path, sys.argv[1:])  # Pass command line args (minus script name) to main()