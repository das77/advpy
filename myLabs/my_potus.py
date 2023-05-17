#!/usr/bin/env python
import sys

# other imports  (standard library, standard non-library, local)
"""
Name: potus.py
Purpose: Exercise 6-1
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

def pres_record(term, name, bdate, ddate, bplace, bstate, tsdate, tedate, party):
    """
    Unpoacks tuple into dict
    :return: dict
    """
    return {"term": int(term), "name": name, "dob": bdate, "died": ddate, "birthplace": f'{bplace}, {bstate}', "term_start": tsdate, "term_end": tedate, "party": party }
def get_info(term : int)-> dict:
    """
    Finds president record for provided term number
    :param term: Number of term
    :return: List or String
    """
    try:
        get_pres = import_file(file_path)
    except Exception as err:
        raise Exception(f'Error importing data from file: {err}') from err
    try:
        pres_info = [pres_record(*data) for data in get_pres if pres_record(*data)['term'] == term]
    except Exception as err:
        raise Exception(f'Error parsing info from provided term: {err}') from err
    if pres_info:
        return  pres_info
    else:
        return 'Term number does not exist'
    return pres_info
