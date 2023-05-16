#!/usr/bin/env python
import sys
from my_functions import convert_date_object
"""
Name: my_ww2_days.py
Purpose: Exercise 2-1
Created By: David Spera
Created Date: 05/15/2023
Modified Date:
"""
# constants (AKA global variables -- keep these to a minimum)
dates = ['December 7, 1941', 'August 15, 1945']

# main function
def main(date_list : list, args):
    """
    Takes a list of date strings and gets the weekday and leap year
    :param date_list: List of date strings
    :param args: Command line arguments.
    :return: None
    """

    date_obj = []
    # parse list and convert str to datetime
    for date in date_list:
        date_obj.append(convert_date_object(date))
    # calc number of days between dates
    num_days = date_obj[1] - date_obj[0]
    print(f'{num_days.days} days')

if __name__ == '__main__':
    main(dates, sys.argv[1:])  # Pass command line args (minus script name) to main()



