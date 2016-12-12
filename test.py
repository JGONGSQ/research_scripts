#!/usr/bin/python

# local imports
from py_files.data import trim_data
from py_files.settings import *

utility_variables = ['ORIGIN']

results = trim_data(
    input_file=TEST_INPUT_DATA_PATH,
    output_file=TEST_OUTPUT_DATA_PATH,
    compulsory_fields=COMPULSORY_FIELDS,
    city_lists=CITY_LISTS,
    city_codes=CITY_CODES,
    utility_parameters=utility_variables
)

print results
