#!/usr/bin/python

# Imports of python packages
from py_files.data import read_file, write_file, read_file_by_city, convert_list_to_str, \
    convert_tuple_to_list, case_config_excluding_variables
from datetime import datetime
import subprocess

# Constants import from settings file
from py_files.settings import *


case_config_list = [1, 4, 7]

start_time = datetime.now()

case_config = 1
results = read_file_by_city(INPUT_DATA_FILE,
                            COMPULSORY_FIELDS,
                            CITY_LISTS,
                            CITY_CODES,
                            UTILITY_VARIABLES,
                            NUMBER_OF_DATA_NEEDED)

# write the file
input_file_path = INPUT_DIR_PATH + '/test_results.csv'
write_file(input_file_path, results)
output_file_path = RESULTS_PATH + '/results' + '_{}'.format(case_config) + '_{}'.format(111111) + '.txt'
print output_file_path

process = subprocess.call(
    ['Rscript --vanilla {r_script_file} {input_file} {number_of_alternatives} {case_config} {utility_parameter} {city_list} {results_file}'.format(
        r_script_file=RUNNER_MDCEV,
        input_file=input_file_path,
        number_of_alternatives=CITY_LISTS.__len__(),
        case_config=case_config,
        utility_parameter=convert_list_to_str(UTILITY_VARIABLES),
        city_list=convert_list_to_str(CITY_LISTS),
        results_file=output_file_path)
    ]
    , shell=True)


print(datetime.now() - start_time)
