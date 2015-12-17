#!/usr/bin/env python3

""" Assignment 3, Exercise 2, INF1340, Fall, 2015. Kanadia

Computer-based immigration office for Kanadia

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

import re
import datetime
import json

######################
## global constants ##
######################
REQUIRED_FIELDS = ["passport", "first_name", "last_name",
                   "birth_date", "home", "entry_reason", "from"]

######################
## global variables ##
######################
'''
countries:
dictionary mapping country codes (lowercase strings) to dictionaries
containing the following keys:
"code","name","visitor_visa_required",
"transit_visa_required","medical_advisory"
'''
COUNTRIES = None


#####################
# HELPER FUNCTIONS ##
#####################
def is_more_than_x_years_ago(x, date_string):
    """
    Check if date is less than x years ago.

    :param x: int representing years
    :param date_string: a date string in format "YYYY-mm-dd"
    :return: True if date is less than x years ago; False otherwise.
    """

    now = datetime.datetime.now()
    x_years_ago = now.replace(year=now.year - x)
    date = datetime.datetime.strptime(date_string, '%Y-%m-%d')

    return (date - x_years_ago).total_seconds() < 0


def decide(input_file, countries_file):
    """
    Decides whether a traveller's entry into Kanadia should be accepted

    :param input_file: The name of a JSON formatted file that contains
        cases to decide
    :param countries_file: The name of a JSON formatted file that contains
        country data, such as whether an entry or transit visa is required,
        and whether there is currently a medical advisory
    :return: List of strings. Possible values of strings are:
        "Accept", "Reject", and "Quarantine"
    """
# call functions to check if person should be rejected
    complete_record()

# if an entry record is incomplete or has an invalid location, reject
    if complete_record() == "Reject":
        return ["Reject"]
    elif valid_location() == "Reject":
        return ["Reject"]
# if someone is "visiting" from a country that requires a visitor's visa,
# check for the visa, if older than two years, reject
    elif needs_visa() == True:
        return ["Reject"]
# if any entrant that has not been rejected, is coming from
# a country with a medical advisory, quarantine:
    elif check_medical_advisory() == "Quarantine":
        return ["Quarantine"]
# if an entrant is not rejected or quarantined after the previous checks, accept
    else:
        return ["Accept"]


# check if any required values in input_file are null
def complete_record(passport, first_name, last_name, birth_date, city, region, country, entry_reason):
    if passport is None:
        return "Reject"
    elif first_name is None:
        return "Reject"
    elif last_name is None:
        return "Reject"
    elif birth_date is None:
        return "Reject"
    elif city is None:
        return "Reject"
    elif region is None:
        return "Reject"
    elif country is None:
        return "Reject"
    elif entry_reason is None:
        return "Reject"
    else:
        return "Maybe"


def valid_location(city, region, country):
    known_cities = ("bala", "weasel", "eureka", "desmond", "a")
    known_regions = ("ON", "Rodent", "NU", "Ohio", "a")
    known_countries = ("KAN", "BRD", "JIK", "LUG")

    if city.lower() in known_cities and region.lower() in known_regions.lower() and country.upper() in known_countries:
        return "Maybe"
    else:
        return "Reject"

def accepted_home_country(home):
    if home.upper() is "KAN":
        return "Maybe"

def needs_visa(entry_reason, visitor_visa_required):
    if entry_reason == "visit" and visitor_visa_required == True:
        is_more_than_x_years_ago(2, visa)

def check_medical_advisory(medical_advisory):
    if medical_advisory is not None:
        return "Quarantine"

def valid_passport_format(passport_number):
    """
    Checks whether a pasport number is five sets of five alpha-number characters separated by dashes
    :param passport_number: alpha-numeric string
    :return: Boolean; True if the format is valid, False otherwise
    """
    return False


def valid_visa_format(visa_code):
    """
    Checks whether a visa code is two groups of five alphanumeric characters
    :param visa_code: alphanumeric string
    :return: Boolean; True if the format is valid, False otherwise

    """


def valid_date_format(date_string):
    """
    Checks whether a date has the format YYYY-mm-dd in numbers
    :param date_string: date to be checked
    :return: Boolean True if the format is valid, False otherwise
    """

    return False