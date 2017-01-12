#!/usr/bin/python

# Imports of python packages
from py_files.data import write_file, read_file_by_city, convert_list_to_str, \
    convert_tuple_to_list, case_config_excluding_variables, get_utility_variables
from datetime import datetime
import subprocess

# Constants import from settings file
from py_files.settings import *


UTILITY_VARIABLES_ALTERNATIVES = [

    # Alternative 2
    ["HOMESUPP", "HOMEREGN", "ORIGIN", "AGEGROUP", "CH15TO24", "LIFECYCLE"],
    # Alternative 3
    ["HOMESUPP", "HOMEREGN", "ORIGIN", "CH15TO24", "MARITAL", "EMPLOYMENT"],
    # ["HOMESUPP", "HOMESLA", "HOMEREGN", "ORIGIN"],
    # ["HOMESUPP", "HOMEREGN", "EMPLOYMENT", "LIFECYCLE"],
    # ["HOMESUPP", "HOMESLA", "HOMEREGN", "ORIGIN", "EMPLOYMENT", "MARITAL"],
    # Alternative 4
    ["HOMESUPP", "HOMEREGN", "AGEGROUP", "EMPLOYMENT"],
    # Alternative 5
    ["HOMESUPP", "HOMEREGN", "AGEGROUP", "EMPLOYMENT", "LIFECYCLE"],
    # Alternative 6
    ["HOMESUPP", "HOMEREGN", "ORIGIN", "AGEGROUP", "MARITAL"]
]


UTILITY_VARIABLES = get_utility_variables(UTILITY_VARIABLES_ALTERNATIVES)

case_config_list = [1, 4, 7]

start_time = datetime.now()

for case_config in case_config_list:

    # write the file
    input_file_path = INPUT_DIR_PATH + '/NVS2007_trimed.csv'

    output_file_path = RESULTS_PATH + '/results' + '_{}'.format(case_config) + '_{}'.format('MDCEV') + '.txt'
    print output_file_path

    process = subprocess.call(
        ['Rscript --vanilla {r_script_file} {input_file} '
         '{number_of_alternatives} {case_config} {utility_parameter} {state_list} {results_file} '
         '{alternative_2_variables} {alternative_3_variables} {alternative_4_variables} '
         '{alternative_5_variables} {alternative_6_variables}'.format(
            r_script_file=RUNNER_MDCEV,
            input_file=input_file_path,
            number_of_alternatives=STATE_LISTS.__len__(),
            case_config=case_config,
            utility_parameter=convert_list_to_str(UTILITY_VARIABLES),
            state_list=convert_list_to_str(STATE_LISTS),
            results_file=output_file_path,
            alternative_2_variables=convert_list_to_str(UTILITY_VARIABLES_ALTERNATIVES[0]),
            alternative_3_variables=convert_list_to_str(UTILITY_VARIABLES_ALTERNATIVES[1]),
            alternative_4_variables=convert_list_to_str(UTILITY_VARIABLES_ALTERNATIVES[2]),
            alternative_5_variables=convert_list_to_str(UTILITY_VARIABLES_ALTERNATIVES[3]),
            alternative_6_variables=convert_list_to_str(UTILITY_VARIABLES_ALTERNATIVES[4]),
        )
        ]
        , shell=True)


print(datetime.now() - start_time)
