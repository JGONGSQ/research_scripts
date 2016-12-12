#!/usr/bin/python

# local imports
from py_files.data import trim_data
from py_files.settings import *

# utility_variables = ['HOMESLA', 'ORIGIN', 'HOUSEHOLD', 'UNDER15', 'OVER15', 'PARENT', 'YOUNGEST', 'AGEGROUP', 'CH15TO24', 'GENDER', 'MARITAL', 'EMPLOYMENT', 'HOUSINC', 'LIFECYCLE']

utility_variables = ['ORIGIN', 'HOMESLA']

results = trim_data(
    input_file=TEST_INPUT_DATA_PATH,
    output_file=TEST_OUTPUT_DATA_PATH,
    compulsory_fields=COMPULSORY_FIELDS,
    city_lists=CITY_LISTS,
    city_codes=CITY_CODES,
    utility_parameters=utility_variables
)

print results
