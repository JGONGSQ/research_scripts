# Path
# DEFAULT_PATH = '/Users/James/Desktop/master_project'

# File
### csv ###
INPUT_DATA_FILE = '../Data/NVS2007unit.csv'
TEST_OUTPUT_FILE = '../Data/test_output_file.csv'
TEST_INPUT_FILE_PATH = '../r_resources/Model_Estimation/az_hhld_vfc_cleaned_final.csv'

RESULTS_PATH = '../Data/results'

### R scripts ###
TEST_R_SCRIPT_FILE = 'r_files/runner.r'
R_MDCEV_SCRIPT = 'r_files/MDCEV.r'

RUNNER_MDCEV = 'r_files/runner_mdcev_nooutside.r'

# Constants
# NUMBER_OF_DATA_NEEDED = 200
NUMBER_OF_DATA_NEEDED = 40000
NUMBER_OF_OUTSIDE_GOODS = 1

# Fields list
PREFIX = ['REGN', 'NITES']

COMPULSORY_FIELDS = ['id', 'uno', 'sero', 'NUMSTOP']

CITY_LISTS = ['Sydney', 'Melbourne', 'Brisbane', 'Adelaide', 'Hobart', 'Darwin']
CITY_CODES = ['104', '201', '302', '404', '601', '801']

UTILITY_VARIABLES = ['ORIGIN']
ALL_VARIABLES = ['HOMESUPP', 'HOMESLA', 'HOMEREGN', 'ORIGIN', 'HOUSEHOLD', 'UNDER15', 'OVER15', 'PARENT', 'YOUNGEST',
                 'AGEGROUP', 'CH15TO24', 'GENDER', 'MARITAL', 'EMPLOYMENT', 'HOUSINC', 'LIFECYCLE']

EXECLUDE_VARIABLE_1 = []
EXECLUDE_VARIABLE_4 = ['YOUNGEST', 'PARENT', 'HOMESUPP', 'HOMESLA', 'HOMEREGN']
EXECLUDE_VARIABLE_7 = []
