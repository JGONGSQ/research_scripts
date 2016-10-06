#!/usr/bin/python

# Imports of python package
from py_files.data import read_file, write_file, read_file_by_city, convert_list_to_str
from datetime import datetime
import subprocess

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
    for item in ALL_VARIABLES:
        variable = list()
        variable.append(item)
        results = read_file_by_city(INPUT_DATA_FILE,
                                    COMPULSORY_FIELDS,
                                    CITY_LISTS,
                                    CITY_CODES,
                                    variable,
                                    NUMBER_OF_DATA_NEEDED)

        # write the file
        write_file(TEST_OUTPUT_FILE, results)
        output_file_path = TEST_RESULTS_FILE + '_{}'.format(case_config) + '_{}'.format(item) + '.csv'
        print output_file_path
        process = subprocess.call(
            ['Rscript --vanilla {r_script_file} {input_file} {number_of_alternatives} {case_config} {utility_parameter} {city_list} {results_file}'.format(
                r_script_file=RUNNER_MDCEV,
                input_file=TEST_OUTPUT_FILE,
                number_of_alternatives=CITY_LISTS.__len__(),
                case_config=case_config,
                utility_parameter=convert_list_to_str(variable),
                city_list=convert_list_to_str(CITY_LISTS),
                results_file=output_file_path)
            ]
            , shell=True)

### Ends ###



### Single Variable Mehtod ###

# Starts #

# case_config = 1
# results = read_file_by_city(INPUT_DATA_FILE,
#                             COMPULSORY_FIELDS,
#                             CITY_LISTS,
#                             CITY_CODES,
#                             UTILITY_VARIABLES,
#                             NUMBER_OF_DATA_NEEDED)
#
# # write the file
# write_file(TEST_OUTPUT_FILE, results)
# output_file_path = TEST_RESULTS_FILE + '_{}'.format(case_config) + '_{}'.format(UTILITY_VARIABLES[0]) + '.csv'
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

