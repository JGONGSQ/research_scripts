#!/usr/bin/python
import subprocess

from py_files.settings import *
from py_files.data import *
from py_files.forecast import *
r_file = 'r_files/forecast/run_mdcev_alpha_forecast.r'
txt_filepath = '/Users/daddyspro/Desktop/useful_results/mutiple_utility_model/results_1_MDCEV_2.txt'
halton_filepath = INPUT_DIR_PATH + '/Halton.csv'
data_filepath = INPUT_DIR_PATH + '/NVS2007_trimed_v3.csv'
results_file = RESULTS_PATH + '/results' + '_{}'.format(1) + '_{}'.format('MDCEV_2') + '.csv'
coef_file = INPUT_DIR_PATH + '/coef.csv'

csv_filepath = convert_txt_to_csv(txt_filepath)
print csv_filepath

# coef_dict = get_coefficient_dict(csv_filepath)
#
# print("This is the dictionary", coef_dict)
# for item in coef_dict:
#     print coef_dict[item]

case_config = 1

process = subprocess.call(
        ['Rscript --vanilla {r_file} {data_file} '
         '{number_of_alternatives} {case_config} {state_list} {results_file} '
         '{halton_file} {coef_file}'.format(
            r_file=r_file,
            data_file=data_filepath, #1
            number_of_alternatives=STATE_LISTS.__len__(),
            case_config=case_config, #3
            state_list=convert_list_to_str(STATE_LISTS),
            results_file=results_file, #5
            halton_file=halton_filepath,
            coef_file=coef_file #7
            )
        ]
        , shell=True)
