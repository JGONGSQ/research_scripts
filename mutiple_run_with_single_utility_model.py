#!/usr/bin/python

# Imports of python packages
from py_files.data import write_file, read_file_by_city, convert_list_to_str, \
    convert_tuple_to_list, case_config_excluding_variables, get_utility_variables, get_utility_parameters_list
from datetime import datetime
from multiprocessing import Pool
import subprocess
import itertools

# Constants import from settings file
from py_files.settings import *

# UTILITY_VARIABLES = ['HOMESUPP', 'HOMESLA', 'HOMEREGN', 'ORIGIN', 'HOUSEHOLD', 'UNDER15',  'EMPLOYMENT', 'AGEGROUP', 'HOUSINC', 'LIFECYCLE', 'OVER15']
# UTILITY_VARIABLES = ['GENDER']
# dropped_variable = [,'LIFECYCLE', 'GENDER', 'MARITAL']
ALL_LOCAL_VARIABLES = ['ORIGIN', 'HOMESLA', 'HOUSEHOLD', 'UNDER15', 'OVER15', 'EMPLOYMENT', 'HOUSINC', 'LIFECYCLE', 'GENDER', 'MARITAL']
case_config_list = [1, 4, 7]

local_variable = ['ORIGIN', 'HOMESLA', 'HOUSEHOLD', 'UNDER15', 'OVER15', 'EMPLOYMENT', 'HOUSINC']

UTILITY_VARIABLES_ALTERNATIVES = [
    # Alternative 2
    local_variable,
    # Alternative 3
    local_variable,
    # Alternative 4
    local_variable,
    # Alternative 5
    local_variable,
    # Alternative 6
    local_variable
]


def cal_estimation(case_config, input_file, results_file, utility_parameter):
    process = subprocess.call(
        ['Rscript --vanilla {r_script_file} {input_file} '
         '{number_of_alternatives} {case_config} {utility_parameter} {city_list} {results_file} '
         '{alternative_2_variables} {alternative_3_variables} {alternative_4_variables} '
         '{alternative_5_variables} {alternative_6_variables}'.format(
            r_script_file=RUNNER_MDCEV,
            input_file=input_file,
            number_of_alternatives=CITY_LISTS.__len__(),
            case_config=case_config,
            utility_parameter=convert_list_to_str(utility_parameter),
            city_list=convert_list_to_str(CITY_LISTS),
            results_file=results_file,
            alternative_2_variables=convert_list_to_str(utility_parameter),
            alternative_3_variables=convert_list_to_str(utility_parameter),
            alternative_4_variables=convert_list_to_str(utility_parameter),
            alternative_5_variables=convert_list_to_str(utility_parameter),
            alternative_6_variables=convert_list_to_str(utility_parameter),
        )

        ]
        , shell=True)
    return process


UTILITY_VARIABLES = get_utility_parameters_list(get_utility_variables(UTILITY_VARIABLES_ALTERNATIVES))


start_time = datetime.now()


list_of_estimations = list()
for case_config in case_config_list:

    # generate the combination of lists
    variable_combinations = itertools.combinations(ALL_LOCAL_VARIABLES, len(ALL_LOCAL_VARIABLES)-1)

    for local_combination in variable_combinations:
        combination = convert_tuple_to_list(local_combination)



        variable_in_names = ''
        for i, item in enumerate(combination):
            variable_in_names += str(item)
            if i != len(combination) -1 :
                variable_in_names += '-'

        input_file = INPUT_DIR_PATH + '/MDCEV_data_v0.csv'
        output_file = RESULTS_PATH + '/results' + '_{}'.format(case_config) + '_{}'.format(variable_in_names) + '.txt'
        list_of_estimations.append((case_config, input_file, output_file, get_utility_parameters_list(combination)))

pool = Pool(processes=6)

for item in list_of_estimations:
    print item
    pool.apply_async(cal_estimation, (item[0], item[1], item[2], item[3]))

pool.close()
pool.join()

# write the file

# output_file_path = RESULTS_PATH + '/results' + '_{}'.format(case_config) + '_{}'.format('MDCEV') + '.txt'


# process = subprocess.call(
#     ['Rscript --vanilla {r_script_file} {input_file} '
#      '{number_of_alternatives} {case_config} {utility_parameter} {city_list} {results_file} '
#      '{alternative_2_variables} {alternative_3_variables} {alternative_4_variables} '
#      '{alternative_5_variables} {alternative_6_variables}'.format(
#         r_script_file=RUNNER_MDCEV,
#         input_file=input_file_path,
#         number_of_alternatives=CITY_LISTS.__len__(),
#         case_config=case_config,
#         utility_parameter=convert_list_to_str(UTILITY_VARIABLES),
#         city_list=convert_list_to_str(CITY_LISTS),
#         results_file=output_file_path,
#         alternative_2_variables=convert_list_to_str(get_utility_parameters_list(UTILITY_VARIABLES_ALTERNATIVES[0])),
#         alternative_3_variables=convert_list_to_str(get_utility_parameters_list(UTILITY_VARIABLES_ALTERNATIVES[1])),
#         alternative_4_variables=convert_list_to_str(get_utility_parameters_list(UTILITY_VARIABLES_ALTERNATIVES[2])),
#         alternative_5_variables=convert_list_to_str(get_utility_parameters_list(UTILITY_VARIABLES_ALTERNATIVES[3])),
#         alternative_6_variables=convert_list_to_str(get_utility_parameters_list(UTILITY_VARIABLES_ALTERNATIVES[4])),
#     )
#
#     ]
#     , shell=True)


print(datetime.now() - start_time)


