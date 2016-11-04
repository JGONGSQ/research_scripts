#!/usr/bin/python

# Imports of python package
from py_files.data import read_file, write_file, read_file_by_city, convert_list_to_str, \
    convert_tuple_to_list, case_config_excluding_variables
from datetime import datetime
import subprocess
import itertools


# All constants are import from settings file
from py_files.settings import *

# This would be a variable for different case, but leave 14 for testing purpose
local_number_of_alternatives = 14
# Same as previous example, leave 4 for testing purpose
case_config_list = [1, 4, 7]
index_of_outside_goods = 167


start_time = datetime.now()

# read the file
# results = read_file(INPUT_DATA_FILE, FIELD_LIST, NUMBER_OF_DATA_NEEDED)

### Multiple Variable Method ###
### Starts ###


for case_config in case_config_list:
    # To exclude the parameter
    list_of_variables = case_config_excluding_variables(case_config)

    # generate the combination of the lists
    variable_combinations = itertools.combinations(list_of_variables, 2)

    for variable_combination in variable_combinations:
        variable_combination = convert_tuple_to_list(variable_combination)
        results = read_file_by_city(INPUT_DATA_FILE, COMPULSORY_FIELDS, CITY_LISTS,
                                    CITY_CODES, variable_combination, NUMBER_OF_DATA_NEEDED)

        # write the file
        write_file(TEST_OUTPUT_FILE, results)

        variable_in_names = ''
        for i, item in enumerate(variable_combination):
            variable_in_names += str(item)
            if i != len(variable_combination)-1:
                variable_in_names += '-'

        output_file_path = RESULTS_PATH + '/results' + '_{}'.format(case_config) + '_{}'.format(variable_in_names) + '.txt'
        print output_file_path
        process = subprocess.call(
            ['Rscript --vanilla {r_script_file} {input_file} {number_of_alternatives} {case_config} {utility_parameter} {city_list} {results_file}'.format(
                r_script_file=RUNNER_MDCEV,
                input_file=TEST_OUTPUT_FILE,
                number_of_alternatives=CITY_LISTS.__len__(),
                case_config=case_config,
                utility_parameter=convert_list_to_str(variable_combination),
                city_list=convert_list_to_str(CITY_LISTS),
                results_file=output_file_path)
            ]
            , shell=True)

### Ends ###



### Single Variable Mehtod ###

# Starts #

# case_config = 4
# results = read_file_by_city(INPUT_DATA_FILE,
#                             COMPULSORY_FIELDS,
#                             CITY_LISTS,
#                             CITY_CODES,
#                             UTILITY_VARIABLES,
#                             NUMBER_OF_DATA_NEEDED)
#
# # write the file
# write_file(TEST_OUTPUT_FILE, results)
# output_file_path = RESULTS_PATH + '/results' + '_{}'.format(case_config) + '_{}'.format(UTILITY_VARIABLES[0]) + '.txt'
# print output_file_path
#
# process = subprocess.call(
#     ['Rscript --vanilla {r_script_file} {input_file} {number_of_alternatives} {case_config} {utility_parameter} {city_list} {results_file}'.format(
#         r_script_file=RUNNER_MDCEV,
#         input_file=TEST_OUTPUT_FILE,
#         number_of_alternatives=CITY_LISTS.__len__(),
#         case_config=case_config,
#         utility_parameter=convert_list_to_str(UTILITY_VARIABLES),
#         city_list=convert_list_to_str(CITY_LISTS),
#         results_file=output_file_path)
#     ]
#     , shell=True)


# Ends #

print(datetime.now() - start_time)

