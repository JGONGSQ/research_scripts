#!/usr/bin/python

from py_files.settings import *
from py_files.data import *
import csv

filepath = '/Users/daddyspro/Desktop/useful_results/mutiple_utility_model/results_1_MDCEV_2.txt'
# 'results_4_MDCEV_2.txt'
# 'results_7_MDCEV_2.txt'
output_filepath = convert_txt_to_csv(filepath)
print output_filepath

coef_dict = get_coefficient_dict(output_filepath)

print("This is the dictionary", coef_dict)
for item in coef_dict:
    print coef_dict[item]
