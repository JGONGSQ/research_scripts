#!/usr/bin/python

# Imports of python packages
from datetime import datetime
from multiprocessing import Pool
import subprocess
import itertools

from py_files.data import convert_list_to_str, convert_tuple_to_list, get_utility_variables, get_utility_parameters_list

# Constants import from settings file
from py_files.settings import *

case_config_list = [1, 4, 7]

# local_variable = ['ORIGIN_NSW', 'ORIGIN_VIC', 'ORIGIN_QLD', 'ORIGIN_SA', 'ORIGIN_WA', 'ORIGIN_TAS', 'GENDER_FEMALE', 'GENDER_MALE', 'MARITAL_COUPLE', 'MARITAL_SINGLE', 'EMPLOYMENT_WORKING', 'EMPLOYMENT_RETIRED', 'EMPLOYMENT_STUDYING', 'HOUSINC_LOW', 'HOUSINC_MEDIUM', 'HOUSINC_HIGH', 'HOUSINC_DONT_KONW', 'LIFECYCLE_SINGLE', 'LIFECYCLE_COUPLE_NO_KIDS', 'LIFECYCLE_COUPLE_WITH_KIDS', 'AGEGROUP_15_29', 'AGEGROUP_30_39', 'AGEGROUP_40_49', 'AGEGROUP_50_59', 'AGEGROUP_60_69']
local_variable = ['GENDER_MALE', 'GENDER_FEMALE', 'MARITAL_SINGLE', 'MARITAL_COUPLE', 'AGEGROUP_15_29', 'AGEGROUP_30_39', 'AGEGROUP_40_49', 'AGEGROUP_50_59', 'AGEGROUP_60_69', 'AGEGROUP_70+', 'PARTYPE_UNACCOMPANIED', 'PARTYPE_ADULT_COUPLE', 'PARTYPE_FAMILY_GROUP', 'PARTYPE_FREIEND_RELATIVES', 'PARTYPE_BUSINESS_ASSOCIATES', 'PARTYPE_SCHOOL_TOUR', 'TRIP_PURPOSE_HOLIDAY', 'TRIP_PURPOSE_VISITING_FR', 'TRIP_PURPOSE_BUSINESS', 'TRIP_PURPOSE_EMPLOYMENT', 'TRIP_PURPOSE_EDUCATION', 'TRIP_PURPOSE_OTHER', 'CUSTOMS_ENTRY_NSW', 'CUSTOMS_ENTRY_VIC', 'CUSTOMS_ENTRY_QLD', 'CUSTOMS_ENTRY_SA', 'CUSTOMS_ENTRY_TAS', 'CUSTOMS_ENTRY_NT', 'CUSTOMS_ENTRY_OTHER']


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
            number_of_alternatives=STATE_LISTS.__len__(),
            case_config=case_config,
            utility_parameter=convert_list_to_str(utility_parameter),
            city_list=convert_list_to_str(STATE_LISTS),
            results_file=results_file,
            alternative_2_variables=convert_list_to_str(utility_parameter),
            alternative_3_variables=convert_list_to_str(utility_parameter),
            alternative_4_variables=convert_list_to_str(utility_parameter),
            alternative_5_variables=convert_list_to_str(utility_parameter),
            alternative_6_variables=convert_list_to_str(utility_parameter),
        )
        ]
        , shell=True
    )
    return process


def generate_list_of_estimations(utility_variables, case_config_list):

    list_of_estimations = list()

    for case_config in case_config_list:

        # generate the combination of lists
        variable_combinations = itertools.combinations(utility_variables, len(utility_variables) - 3)

        for local_combination in variable_combinations:
            combination = convert_tuple_to_list(local_combination)

            variable_in_names = ''
            for i, item in enumerate(combination):
                variable_in_names += str(item)
                if i != len(combination) - 1:
                    variable_in_names += '-'

            input_file = '../Data/ivs/filted_data.csv'
            output_file = RESULTS_PATH + '/ivs/results' + '_{}'.format(case_config) + '_{}'.format(variable_in_names) + '.txt'
            list_of_estimations.append((case_config, input_file, output_file, get_utility_parameters_list(combination)))

    return list_of_estimations


def run_estimation_with_multiprocessing(list_of_estimations):
    pool = Pool(processes=6)

    for estimation in list_of_estimations:
        pool.apply_async(cal_estimation, (estimation[0], estimation[1], estimation[2], estimation[3]))

    pool.close()
    pool.join()
    return


if __name__ == '__main__':
    # Start of timing
    start_time = datetime.now()

    # Get the utilituy variables
    utility_variables = get_utility_parameters_list(get_utility_variables(UTILITY_VARIABLES_ALTERNATIVES))

    # Generate list of estimations
    list_of_estimations = generate_list_of_estimations(utility_variables, case_config_list)

    # Run estimation with multiprocessing
    run_estimation_with_multiprocessing(list_of_estimations=list_of_estimations)
    # print(len(local_variable))

    # End of timing
    print(datetime.now() - start_time)


