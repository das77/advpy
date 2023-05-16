from dateutil import parser

"""
Name: my_functions.py
Purpose: Re-usable functions
Created By: David Spera
Created Date: 05/15/2023
Modified Date:
"""

def convert_date_object(date_str : str):
    """
    converts a string to a datetime object
    :type date_str: object
    :return: datetime object
    """
    try:
        dt = parser.parse(date_str)
    except ValueError as err:
        print(f"Can't parse: {date_str}")
    return dt