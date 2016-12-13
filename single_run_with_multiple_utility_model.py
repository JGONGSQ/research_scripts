#!/usr/bin/python

# Imports of python packages
from py_files.data import write_file, read_file_by_city, convert_list_to_str, \
    convert_tuple_to_list, case_config_excluding_variables, get_utility_variables
from datetime import datetime
import subprocess

# Constants import from settings file
from py_files.settings import *

# UTILITY_VARIABLES = ['HOMESUPP', 'HOMESLA', 'HOMEREGN', 'ORIGIN', 'HOUSEHOLD', 'UNDER15',  'EMPLOYMENT', 'AGEGROUP', 'HOUSINC', 'LIFECYCLE', 'OVER15']
# UTILITY_VARIABLES = ['GENDER']


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

case_config_list = [1]

start_time = datetime.now()

case_config = 7
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
    ['Rscript --vanilla {r_script_file} {input_file} '
     '{number_of_alternatives} {case_config} {utility_parameter} {city_list} {results_file} '
     '{alternative_2_variables} {alternative_3_variables} {alternative_4_variables} '
     '{alternative_5_variables} {alternative_6_variables}'.format(
        r_script_file=RUNNER_MDCEV,
        input_file=input_file_path,
        number_of_alternatives=CITY_LISTS.__len__(),
        case_config=case_config,
        utility_parameter=convert_list_to_str(UTILITY_VARIABLES),
        city_list=convert_list_to_str(CITY_LISTS),
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
