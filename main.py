#!/usr/bin/python

# Imports of python package
from data import read_file, write_file
import subprocess

# All constants are import from settings file
from settings import *


# read the file
results = read_file(INPUT_DATA_FILE, FIELD_LIST, NUMBER_OF_DATA_NEEDED)

# write the file
write_file(TEST_OUTPUT_FILE, results)


# subprocess.call(['Rscript --vanilla {r_script_file} arg1 arg2 arg3'.format(r_script_file=TEST_R_SCRIPT_FILE)], shell=True)