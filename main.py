#!/usr/bin/python

# Imports of python package
from py_files.data import read_file, write_file, read_file_by_city, convert_list_to_str, \
    convert_tuple_to_list, case_config_excluding_variables
from datetime import datetime
from multiprocessing import Pool
import subprocess
import itertools



# All constants are import from settings file
from py_files.settings import *


# Same as previous example, leave 4 for testing purpose
case_config_list = [1, 4, 7]
index_of_outside_goods = 167


start_time = datetime.now()

### Multiple Variable Method ###
### Starts ###


def cal_estimation(case_config, input_file, results_file, utility_parameter):
    process = subprocess.call(
        [
            'Rscript --vanilla {r_script_file} {input_file} {number_of_alternatives} {case_config} {utility_parameter} {city_list} {results_file}'.format(
                r_script_file=RUNNER_MDCEV,
                input_file=input_file,
                number_of_alternatives=CITY_LISTS.__len__(),
                case_config=case_config,
                utility_parameter=utility_parameter,
                city_list=convert_list_to_str(CITY_LISTS),
                results_file=results_file)
        ]
        , shell=True)

    return process

list_of_estimations = list()

# Generate all names and files required for estimation
for case_config in case_config_list:
    # To exclude the parameter
    list_of_variables = case_config_excluding_variables(case_config)

    # generate the combination of the lists
    variable_combinations = itertools.combinations(list_of_variables, len(list_of_variables)-3)

    for variable_combination in variable_combinations:
        variable_combination = convert_tuple_to_list(variable_combination)
        results = read_file_by_city(INPUT_DATA_FILE, COMPULSORY_FIELDS, CITY_LISTS,
                                    CITY_CODES, variable_combination, NUMBER_OF_DATA_NEEDED)

        variable_in_names = ''
        for i, item in enumerate(variable_combination):
            variable_in_names += str(item)
            if i != len(variable_combination) - 1:
                variable_in_names += '-'

        # write the file
        input_file_path = INPUT_DIR_PATH + '/input' + '_{}'.format(case_config) + '_{}'.format(variable_in_names) + '.csv'
        write_file(input_file_path, results)

        output_file_path = RESULTS_PATH + '/results' + '_{}'.format(case_config) + '_{}'.format(variable_in_names) + '.txt'
        list_of_estimations.append((case_config, input_file_path, output_file_path, convert_list_to_str(variable_combination)))

# multiprocessing CAREFUL, DANGEROURS !!!!!! Monster !!!!!
pool = Pool(processes=6)
for item in list_of_estimations:
    print item
    pool.apply_async(cal_estimation, (item[0], item[1], item[2], item[3]))
pool.close()
pool.join()


#
# for case_config in case_config_list:
#     # To exclude the parameter
#     list_of_variables = case_config_excluding_variables(case_config)
#
#     # generate the combination of the lists
#     variable_combinations = itertools.combinations(list_of_variables, 2)
#
#     for variable_combination in variable_combinations:
#         variable_combination = convert_tuple_to_list(variable_combination)
#         results = read_file_by_city(INPUT_DATA_FILE, COMPULSORY_FIELDS, CITY_LISTS,
#                                     CITY_CODES, variable_combination, NUMBER_OF_DATA_NEEDED)
#
#         # write the file
#         write_file(TEST_OUTPUT_FILE, results)
#
#         variable_in_names = ''
#         for i, item in enumerate(variable_combination):
#             variable_in_names += str(item)
#             if i != len(variable_combination)-1:
#                 variable_in_names += '-'
#
#         output_file_path = RESULTS_PATH + '/results' + '_{}'.format(case_config) + '_{}'.format(variable_in_names) + '.txt'
#         print output_file_path
#         process = subprocess.call(
#             ['Rscript --vanilla {r_script_file} {input_file} {number_of_alternatives} {case_config} {utility_parameter} {city_list} {results_file}'.format(
#                 r_script_file=RUNNER_MDCEV,
#                 input_file=TEST_OUTPUT_FILE,
#                 number_of_alternatives=CITY_LISTS.__len__(),
#                 case_config=case_config,
#                 utility_parameter=convert_list_to_str(variable_combination),
#                 city_list=convert_list_to_str(CITY_LISTS),
#                 results_file=output_file_path)
#             ]
#             , shell=True)

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
# input_file_path = INPUT_DIR_PATH + '/test_results.csv'
# write_file(input_file_path, results)
# output_file_path = RESULTS_PATH + '/results' + '_{}'.format(case_config) + '_{}'.format(111111) + '.txt'
# print output_file_path
#
# process = subprocess.call(
#     ['Rscript --vanilla {r_script_file} {input_file} {number_of_alternatives} {case_config} {utility_parameter} {city_list} {results_file}'.format(
#         r_script_file=RUNNER_MDCEV,
#         input_file=input_file_path,
#         number_of_alternatives=CITY_LISTS.__len__(),
#         case_config=case_config,
#         utility_parameter=convert_list_to_str(UTILITY_VARIABLES),
#         city_list=convert_list_to_str(CITY_LISTS),
#         results_file=output_file_path)
#     ]
#     , shell=True)


# Ends #

print(datetime.now() - start_time)

