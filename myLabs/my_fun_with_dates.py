#!/usr/bin/env python
import sys
import calendar
from my_functions import convert_date_object

"""
Name: my_fun_with_dates.py
Purpose: Exercise 3-3
Created By: David Spera
Created Date: 05/15/2023
Modified Date:  
"""

# constants (AKA global variables -- keep these to a minimum)
dates = ['October 31, 1956', 'September 22, 1952', 'August 27, 1990']

# other functions
def get_day_of_week(date : object):
    """
    Takes a datetime object and finds the day of week
    :type date: object
    :param date: datetime object
    :return: string
    """
    try:
        day = date.strftime("%A")
    except Exception as err:
        print(f"Can't parse weekday from: {date}")
    return day

def check_leap(year : str):
    """
    Takes a year and checks for leap year
    :type year: object
    :param year: Year in string format
    :return: string
    """
    try:
        leap_year = calendar.isleap(int(year))
    except Exception as err:
        print(f"Unable to check leap year from: {year}")
    if leap_year:
        return 'is'
    else:
        return 'is not'
# main function
def main(date_list, args):
    """
    Takes a list of date strings and gets the weekday and leap year
    :param args:
    :param date_list: List of date strings
    :return: None
    """
    # parse list
    for date in date_list:
        # convert str to datetime
        convert_date = convert_date_object(date)
        # get weekday from datetime object
        weekday = get_day_of_week(convert_date)
        # check for leap year
        leap_year = check_leap(convert_date.strftime("%Y"))
        print(f'{date} is a {weekday} and {leap_year} a leap year')

if __name__ == '__main__':
    main(dates, sys.argv[1:])  # Pass command line args (minus script name) to main()



