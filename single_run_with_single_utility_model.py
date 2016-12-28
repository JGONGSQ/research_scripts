#!/usr/bin/python

# Imports of python packages
from py_files.data import write_file, read_file_by_city, convert_list_to_str, \
    convert_tuple_to_list, case_config_excluding_variables, get_utility_variables, get_utility_parameters_list
from datetime import datetime
import subprocess

# Constants import from settings file
from py_files.settings import *

# UTILITY_VARIABLES = ['HOMESUPP', 'HOMESLA', 'HOMEREGN', 'ORIGIN', 'HOUSEHOLD', 'UNDER15',  'EMPLOYMENT', 'AGEGROUP', 'HOUSINC', 'LIFECYCLE', 'OVER15']
# UTILITY_VARIABLES = ['GENDER']
# dropped_variable = [, 'LIFECYCLE', 'GENDER', 'MARITAL']

# local_variable = ['ORIGIN', 'HOMESLA', 'HOUSEHOLD', 'UNDER15', 'OVER15', 'EMPLOYMENT', 'HOUSINC']
local_variable = ['MARITAL_REFUSED']
# 'MARITAL_REFUSED' , MARITAL_COUPLE MARITAL_SINGLE

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


UTILITY_VARIABLES = get_utility_parameters_list(get_utility_variables(UTILITY_VARIABLES_ALTERNATIVES))

case_config_list = [1]

start_time = datetime.now()

case_config = 1

# write the file
input_file_path = INPUT_DIR_PATH + '/NVS2007_trimed.csv'
# input_file_path = TEST_OUTPUT_DATA_PATH
output_file_path = RESULTS_PATH + '/results' + '_{}'.format(case_config) + '_{}'.format('MDCEV') + '.txt'
print output_file_path

process = subprocess.call(
    ['Rscript --vanilla {r_script_file} {input_file} '
     '{number_of_alternatives} {case_config} {utility_parameter} {city_list} {results_file} '
     '{alternative_2_variables} {alternative_3_variables} {alternative_4_variables} '
     '{alternative_5_variables} {alternative_6_variables}'.format(
        r_script_file=RUNNER_MDCEV,
        input_file=input_file_path,
        number_of_alternatives=STATE_LISTS.__len__(),
        case_config=case_config,
        utility_parameter=convert_list_to_str(UTILITY_VARIABLES),
        city_list=convert_list_to_str(STATE_LISTS),
        results_file=output_file_path,
        alternative_2_variables=convert_list_to_str(get_utility_parameters_list(UTILITY_VARIABLES_ALTERNATIVES[0])),
        alternative_3_variables=convert_list_to_str(get_utility_parameters_list(UTILITY_VARIABLES_ALTERNATIVES[1])),
        alternative_4_variables=convert_list_to_str(get_utility_parameters_list(UTILITY_VARIABLES_ALTERNATIVES[2])),
        alternative_5_variables=convert_list_to_str(get_utility_parameters_list(UTILITY_VARIABLES_ALTERNATIVES[3])),
        alternative_6_variables=convert_list_to_str(get_utility_parameters_list(UTILITY_VARIABLES_ALTERNATIVES[4])),
    )
    ]
    , shell=True)


print(datetime.now() - start_time)


storage_list = ['ORIGIN_NSW', 'ORIGIN_VIC', 'ORIGIN_QLD', 'ORIGIN_SA', 'ORIGIN_WA', 'ORIGIN_TAS', 'GENDER_FEMALE', 'GENDER_MALE', 'MARITAL_COUPLE', 'MARITAL_SINGLE', 'EMPLOYMENT_WORKING', 'EMPLOYMENT_RETIRED', 'EMPLOYMENT_STUDYING', 'HOUSINC_LOW', 'HOUSINC_MEDIUM', 'HOUSINC_HIGH', 'HOUSINC_DONT_KONW', 'LIFECYCLE_SINGLE', 'LIFECYCLE_COUPLE_NO_KIDS', 'LIFECYCLE_COUPLE_WITH_KIDS', 'AGEGROUP_15_29', 'AGEGROUP_30_39', 'AGEGROUP_40_49', 'AGEGROUP_50_59', 'AGEGROUP_60_69']

