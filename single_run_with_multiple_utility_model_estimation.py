#!/usr/bin/python

# Imports of python packages
from py_files.data import write_data_to_csv, read_file_by_city, convert_list_to_str, \
    convert_tuple_to_list, case_config_excluding_variables, get_utility_variables
from datetime import datetime
import subprocess

# Constants import from settings file
from py_files.settings import *

melbourne = ['AGEGROUP_15_29', 'AGEGROUP_40_49', 'HOUSINC_HIGH', 'LIFECYCLE_SINGLE', 'LIFECYCLE_COUPLE_NO_KIDS', 'MARITAL_SINGLE', 'ORIGIN_NSW', 'ORIGIN_QLD', 'ORIGIN_SA', 'ORIGIN_WA', 'ORIGIN_TAS', 'HOUSEHOLD']

brisbane = ['AGEGROUP_60_69', 'GENDER_MALE', 'HOUSINC_LOW', 'HOUSINC_MEDIUM', 'HOUSINC_HIGH', 'LIFECYCLE_COUPLE_NO_KIDS', 'LIFECYCLE_COUPLE_WITH_KIDS', 'DISTANCE_TO_QLD']

adelaide = ['AGEGROUP_15_29', 'AGEGROUP_30_39', 'AGEGROUP_60_69', 'EMPLOYMENT_WORKING', 'EMPLOYMENT_RETIRED', 'EMPLOYMENT_STUDYING', 'GENDER_MALE', 'ORIGIN_NSW', 'ORIGIN_VIC', 'ORIGIN_QLD', 'ORIGIN_SA', 'ORIGIN_TAS', ]

hobart = ['AGEGROUP_40_49', 'AGEGROUP_50_59', 'EMPLOYMENT_RETIRED', 'HOUSINC_LOW', 'HOUSINC_MEDIUM', 'LIFECYCLE_SINGLE', 'LIFECYCLE_COUPLE_NO_KIDS', 'MARITAL_SINGLE', 'ORIGIN_NSW', 'ORIGIN_VIC', 'ORIGIN_SA', 'ORIGIN_WA', 'ORIGIN_TAS', 'DISTANCE_TO_TAS']

darwin = ['AGEGROUP_60_69', 'EMPLOYMENT_WORKING', 'EMPLOYMENT_STUDYING', 'ORIGIN_NSW', 'ORIGIN_VIC', 'ORIGIN_QLD', 'ORIGIN_SA', 'ORIGIN_WA', 'ORIGIN_TAS', 'DISTANCE_TO_NT']

# initial the explanatory variables
UTILITY_VARIABLES_ALTERNATIVES = [
    # Alternative 2
    melbourne,
    # Alternative 3
    brisbane,
    # Alternative 4
    adelaide,
    # Alternative 5
    hobart,
    # Alternative 6
    darwin,
]


UTILITY_VARIABLES = get_utility_variables(UTILITY_VARIABLES_ALTERNATIVES)

case_config_list = [1, 4, 7]

start_time = datetime.now()


for case_config in case_config_list:

    # write the file
    input_file_path = INPUT_DIR_PATH + '/NVS2007_trimed_v3.csv'

    estimation_output_file = RESULTS_PATH + '/results' + '_{}'.format(case_config) + '_{}'.format('MDCEV_2') + '.txt'
    forecast_output_file = RESULTS_PATH + '/results' + '_{}'.format(case_config) + '_{}'.format('MDCEV_2') + '.txt'
    print estimation_output_file

    process = subprocess.call(
        ['Rscript --vanilla {r_script_file} {input_file} '
         '{number_of_alternatives} {case_config} {utility_parameters} {state_list} {results_file} '
         '{alternative_2_variables} {alternative_3_variables} {alternative_4_variables} '
         '{alternative_5_variables} {alternative_6_variables}'.format(
            r_script_file=RUNNER_MDCEV,
            input_file=input_file_path,
            number_of_alternatives=STATE_LISTS.__len__(),
            case_config=case_config,
            utility_parameters=convert_list_to_str(UTILITY_VARIABLES),
            state_list=convert_list_to_str(STATE_LISTS),
            results_file=estimation_output_file,
            alternative_2_variables=convert_list_to_str(UTILITY_VARIABLES_ALTERNATIVES[0]),
            alternative_3_variables=convert_list_to_str(UTILITY_VARIABLES_ALTERNATIVES[1]),
            alternative_4_variables=convert_list_to_str(UTILITY_VARIABLES_ALTERNATIVES[2]),
            alternative_5_variables=convert_list_to_str(UTILITY_VARIABLES_ALTERNATIVES[3]),
            alternative_6_variables=convert_list_to_str(UTILITY_VARIABLES_ALTERNATIVES[4]),
        )
        ]
        , shell=True)
    if case_config == 1:
        print("In the case config 1")
    elif case_config == 4:
        print("In the case config 4")
    elif case_config == 7:
        print("In the case config 7")


print(datetime.now() - start_time)
