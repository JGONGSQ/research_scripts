#!/usr/bin/python

# local imports
from py_files.data import trim_data, find_index_in_list
from py_files.settings import *


output_list = COMPULSORY_FIELDS + CITY_LISTS + ORIGIN_LIST
utility_variable = ['ORIGIN']

results = trim_data(input_file=TEST_INPUT_DATA_PATH, output_file=TEST_OUTPUT_DATA_PATH, output_list=output_list, utility_parameter=utility_variable)

print results
