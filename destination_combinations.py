#!/usr/bin/python

# local imports

from py_files.data import  read_combinations
from py_files.settings import *


results = read_combinations(
    input_file=TEST_INPUT_DATA_PATH,
    output_file=TEST_OUTPUT_DATA_PATH,
    compulsory_fields=COMPULSORY_FIELDS,
    state_lists=STATE_LISTS,
    state_codes=STATE_CODES,
)