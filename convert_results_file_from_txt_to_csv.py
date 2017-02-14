#!/usr/bin/python

from py_files.settings import *
from py_files.data import *
import csv

filepath = '/Users/daddyspro/Desktop/useful_results/mutiple_utility_model/results_1_MDCEV_2.txt'
# 'results_4_MDCEV_2.txt'
# 'results_7_MDCEV_2.txt'
output_filepath = convert_txt_to_csv(filepath)
print output_filepath

coeff_dict = get_coefficient_dict(output_filepath)

print("This is the dictionary", coeff_dict)
for item in coeff_dict:
    print coeff_dict[item]

# test_dict = {
#     "alternative_one": {
#         "variable_one": {
#             "name": "test variable",
#             "value": "123"
#         },
#         "variable_two": {
#             "name": "test variable",
#             "value": "123"
#         }
#
#     },
#
#     "alternative_two": {
#         "variable_one": {
#             "name": "test variable",
#             "value": "123"
#         },
#         "variable_two": {
#             "name": "test variable",
#             "value": "123"
#         }
#
#     }
# }
#
# for item in test_dict:
#     print test_dict[item]