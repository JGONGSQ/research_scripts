#!/usr/bin/python

from py_files.settings import *
from py_files.data import *
import csv

# filter the file to see if converge or not
input_file_path = '/Users/daddyspro/Desktop/useful_results/mutiple_utility_model/results_7_MDCEV_2.txt'
# 'results_4_MDCEV_2.txt'
# 'results_7_MDCEV_2.txt'

output_file_path = '/Users/daddyspro/Desktop/useful_results/mutiple_utility_model/results_7_MDCEV_2.csv'


def read_the_file(input_filepath, output_filepath):
    with open(output_filepath, 'wb') as csvfile:
        row_writer = csv.writer(csvfile, delimiter=',')
        file = open(input_filepath, 'r')

        for line in file:
            row = filter(None, line.split(' '))
            row_writer.writerow(row)


read_the_file(input_file_path, output_file_path)

