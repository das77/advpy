#!/usr/bin/env python
"""
Name: potus_main.py
Purpose: Exercise
Created By: David Spera
Created Date: 05/17/2023
Modified Date:
"""
from my_potus import get_info
# other imports  (standard library, standard non-library, local)

# constants (AKA global variables -- keep these to a minimum)
FILE_PATH = '../DATA/presidents.txt'
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
        m_term = []
        for line in file:
            (
                term, _, _, _, _, _, _, _, _, _
            ) = line[:-1].split(':')
            m_term.append(int(term))
    return max(m_term)
# main function
def main():
    """
    Requests term number from user and returns President info
    :param args: Command line arguments.
    :return: None
    """
    max_term = import_file(FILE_PATH)
    loop = True
    while loop:
        try:
            term = int(input('Enter in term number of president: '))
            if term > max_term or term == 0:
                print('Term does not exist, try again')
            else:
                loop = False
        except ValueError:
            print('Must be a whole number, try again')
    try:
        president = get_info(FILE_PATH, term)
    except FileNotFoundError:
        print(f"File '{FILE_PATH}' not found.")
        return
    except ValueError:
        print("Invalid value for 'term'.")
        return
    except (IOError, PermissionError):
        print("An I/O or permission error occurred.")
        return
    if isinstance(president, list):
        print(president[0])
    else:
        print(president)

if __name__ == '__main__':
    main()  # Pass command line args (minus script name) to main()
