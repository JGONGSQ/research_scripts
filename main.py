#!/usr/bin/python

# Imports of python package
from py_files.data import read_file, write_file
from datetime import datetime
import subprocess

# All constants are import from settings file
from py_files.settings import *

# This would be a variable for different case, but leave 14 for testing purpose
local_number_of_alternatives = 14
# Same as previous example, leave 4 for testing purpose
local_case_config = 4
index_of_outside_goods = 167


start_time = datetime.now()

# read the file
results = read_file(INPUT_DATA_FILE, FIELD_LIST, NUMBER_OF_DATA_NEEDED)

# write the file
write_file(TEST_OUTPUT_FILE, results)


command_line_output = subprocess.call(
    ['Rscript --vanilla {r_script_file} '
     '{input_file_path} {number_of_outside_goods} {number_of_alternatives} {case_config} {index_of_outside_goods}'.format(
        r_script_file=TEST_R_SCRIPT_FILE,
        input_file_path=TEST_INPUT_FILE_PATH,
        number_of_outside_goods=NUMBER_OF_OUTSIDE_GOODS,
        number_of_alternatives=local_number_of_alternatives,
        case_config=local_case_config,
        index_of_outside_goods=index_of_outside_goods)
    ]
    , shell=True)

print(datetime.now() - start_time)
