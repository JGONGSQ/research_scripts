#!/usr/bin/python

# local imports

from py_files.data import read_state_combinations
from py_files.settings import *
# Dropped Varibales
# 'YOUNGEST', 'PARENT'
utility_variables = ['ORIGIN', 'HOUSEHOLD', 'UNDER15', 'OVER15', 'EMPLOYMENT', 'HOUSINC','GENDER','MARITAL','LIFECYCLE','AGEGROUP', 'CH15TO24']

results = read_state_combinations(
    input_file=TEST_INPUT_DATA_PATH,
    output_file=TEST_OUTPUT_DATA_PATH,
    compulsory_fields=COMPULSORY_FIELDS,
    state_lists=STATE_LISTS,
    state_codes=STATE_CODES,
    distance_destination_list=DISTANCE_DESTINATION_LIST,
    utility_parameters=utility_variables
)
