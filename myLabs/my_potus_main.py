#!/usr/bin/env python
import sys
from my_potus import get_info
# other imports  (standard library, standard non-library, local)
"""
Name: potus_main.py
Purpose: Exercise
Created By: David Spera
Created Date: 05/17/2023
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
    all_pres = []
    with open(filename) as file:
        m_term = []
        for line in file:
            (
                term, lname, fname, bdate, ddate, bplace, bstate, tsdate, tedate,
                party
            ) = line[:-1].split(':')
            m_term.append(int(term))
    return max(m_term)
# main function
def main(args):
    """
    Requests term number from user and returns President info
    :param args: Command line arguments.
    :return: None
    """
    max_term = import_file(file_path)
    loop = True
    while loop:
        try:
            term = int(input('Enter in term number of president: '))
            if term > max_term or term == 0:
                print('Term does not exist, try again')
            else:
                loop = False
        except ValueError as err:
            print('Must be a whole number, try again')
    try:
        president = get_info(file_path, term)
    except Exception as err:
        print(err)
        return
    if isinstance(president, list):
        print(president[0])
    else:
        print(president)

if __name__ == '__main__':
    main(sys.argv[1:])  # Pass command line args (minus script name) to main()