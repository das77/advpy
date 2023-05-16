#!/usr/bin/env python
import sys

"""
Name: my_path_files.py
Purpose: Exercise 2-1
Created By: David Spera
Created Date: 05/15/2023
Modified Date:
"""
# other imports  (standard library, standard non-library, local)

# constants (AKA global variables -- keep these to a minimum)

# other functions
def count_files():
    """
    This is the docstring for function1().
    :return: None
    """
    import os

    # Get the PATH environment variable and split it into separate paths
    path = os.getenv('PATH')
    path_list = path.split(os.pathsep)
    data = []

    # Loop through each path and count the number of files in each component
    for p in path_list:
        try:
            num_files = len(os.listdir(p))
        except FileNotFoundError:
            num_files = 0
        data.append(f'{p}: {num_files} files')
    return data

# main function
def main(args):
    """
    This is the docstring for the main() function

    :param args: Command line arguments.
    :return: None
    """
    data = count_files()
    for x in data:
        print(x)

if __name__ == '__main__':
    main(sys.argv[1:])  # Pass command line args (minus script name) to main()