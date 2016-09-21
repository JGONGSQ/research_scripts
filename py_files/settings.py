# Path
# DEFAULT_PATH = '/Users/James/Desktop/master_project'

# File
### csv
INPUT_DATA_FILE = '../Data/NVS2007unit.csv'
TEST_OUTPUT_FILE = '../Data/test_output_file.csv'
TEST_INPUT_FILE_PATH = '../r_resources/Model_Estimation/az_hhld_vfc_cleaned_final.csv'

### R scripts
TEST_R_SCRIPT_FILE = 'r_files/runner.r'
R_MDCEV_SCRIPT = 'r_files/MDCEV.r'

# Constants
# NUMBER_OF_DATA_NEEDED = 200
NUMBER_OF_DATA_NEEDED = 40000
NUMBER_OF_OUTSIDE_GOODS = 1

# Fields list
# FIELD_LIST = ['id', 'uno', 'sero', 'WT', 'NUMSTOP', 'stop']
PREFIX = ['REGN', 'NITES']

COMPULSORY_FIELDS = ['id', 'uno', 'sero', 'NUMSTOP']

CITY_LISTS = ['Sydney', 'Melbourne', 'Brisbane', 'Adelaide', 'Perth', 'Hobart', 'Darwin']
CITY_CODES = ['104', '201', '302', '404', '507', '601', '801']

UTILITY_PARAMETERS = ['HOMESLA', 'HOUSEHOLD', 'GENDER', 'stop']

# FIELD_LIST = COMPULSORY_FIELDS + CITY_LISTS + UTILITY_PARAMETERS