#!/usr/bin/python

# Path
DEFAULT_PATH = '/Users/James/Desktop/master_project'

# File
### csv
INPUT_DATA_FILE = DEFAULT_PATH + '/Data/NVS2007unit.csv'
TEST_OUTPUT_FILE = DEFAULT_PATH + '/Data/test_output_file.csv'
TEST_INPUT_FILE_PATH = DEFAULT_PATH + '/r_resources/Model_Estimation/az_hhld_vfc_cleaned_final.csv'

### R scripts
TEST_R_SCRIPT_FILE = DEFAULT_PATH + '/research_scripts/test_r.r'
R_MDCEV_SCRIPT = '/research_scripts/MDCEV.r'

# Constants
NUMBER_OF_DATA_NEEDED = 100
NUMBER_OF_OUTSIDE_GOODS = 1

# Fields list
FIELD_LIST = ['ID', 'WT', 'NUMSTOP', 'stop']