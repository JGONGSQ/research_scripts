#!/usr/bin/python

from py_files.settings import *
from py_files.data import *


test_file = 'results_4_HOMEREGN.txt'

# filter_files(RESULTS_PATH)
# value = is_file_converge(RESULTS_PATH + '/' + test_file)
# print('Value:', value)
print(ALL_VARIABLES)
print(EXECLUDE_VARIABLE_4)
print(list(set(ALL_VARIABLES).difference(set(EXECLUDE_VARIABLE_1))))
