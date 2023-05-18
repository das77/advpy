#!/usr/bin/env python

# other imports  (standard library, standard non-library, local)
"""
Name: potus.py
Purpose: Exercise 6-1
Created By: David Spera
Created Date: 05/17/2023
Modified Date:
"""

# other functions
def import_file(filename : str):
    """
    Imports file and parses data
    :type filename: object
    :param filename: String of path to file
    :return: tuple
    """
    # import data file
    all_pres = []
    with open(filename) as file:
        for line in file:
            (
                term, lname, fname, bdate, ddate, bplace, bstate, tsdate, tedate,
                party
            ) = line[:-1].split(':')
            name = f'{fname} {lname}'
            if ddate.upper() == 'NONE':
                ddate = '***'
            all_pres.append((term, name, bdate, ddate, bplace, bstate, tsdate, tedate, party))
    return all_pres

def pres_record(record):
    """
    Unpacks tuple into dict
    :return: dict
    """
    term, name, bdate, ddate, bplace, bstate, tsdate, tedate, party = record
    return {
        "term": int(term),
        "name": name,
        "dob": bdate,
        "died": ddate,
        "birthplace": f'{bplace}, {bstate}',
        "term_start": tsdate,
        "term_end": tedate,
        "party": party
    }

def get_info(file : str, term : int)-> list:
    """
    Finds president record for provided term number
    :param file: Path to file to import
    :param term: Number of term
    :return: List or String
    """
    try:
        get_pres = import_file(file)
    except FileNotFoundError as err:
        raise FileNotFoundError from err
    except ValueError as err:
        raise ValueError from err
    except PermissionError as err:
        raise PermissionError from err
    except IOError as err:
        raise IOError from err
    try:
        pres_info = [pres_record(*data) for data in get_pres if pres_record(*data)['term'] == term]
    except Exception as err:
        raise Exception(f'Error parsing info from provided term: {err}') from err
    return  pres_info
