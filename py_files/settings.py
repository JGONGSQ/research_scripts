# Path
# DEFAULT_PATH = '/Users/James/Desktop/master_project'

# File
### csv ###
# INPUT_DATA_FILE = '../Data/NVS2007.csv'
INPUT_DIR_PATH = '../Data/input_files'
TEST_INPUT_FILE_PATH = '../r_resources/Model_Estimation/az_hhld_vfc_cleaned_final.csv'

# NEW ADDED DATA FILE
# TEST_INPUT_DATA_PATH = '../Data/NVS2007unit.csv'
TEST_INPUT_DATA_PATH = '../Data/NVS2006modified.csv'
TEST_OUTPUT_DATA_PATH = '../Data/test_output_file.csv'
REGN_CODE_DICT_PATH = '../Data/regn_code_dict.csv'
REGN_CODE_DICT_PATH_V1 = '../Data/regn_code_dict_v1.csv'
REGN_CODE_DICT_PATH_V2 = '../Data/regn_code_dict_v2.csv'


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

STATE_FULL = ['New South Wales', 'Victoria', 'Queensland', 'South Australia', 'Tasmania', 'Northern Territory']
STATE_LISTS = ['NSW', 'VIC', 'QLD', 'SA', 'TAS', 'NT']
STATE_CODES = ['1', '2', '3', '4', '6', '8']

##
# ALL_VARIABLES = ['HOMESUPP', 'HOMESLA', 'HOMEREGN', 'ORIGIN', 'HOUSEHOLD', 'UNDER15', 'OVER15', 'PARENT', 'YOUNGEST',
#                  'AGEGROUP', 'CH15TO24', 'GENDER', 'MARITAL', 'EMPLOYMENT', 'HOUSINC', 'LIFECYCLE']
ALL_VARIABLES = ['HOMESUPP', 'HOMESLA', 'HOMEREGN', 'ORIGIN', 'UNDER15', 'OVER15', 'PARENT', 'YOUNGEST',
                 'AGEGROUP', 'CH15TO24', 'GENDER', 'MARITAL', 'EMPLOYMENT', 'HOUSINC', 'LIFECYCLE']
##
# UTILITY_VARIABLES = ['HOMESUPP', 'HOMESLA', 'HOMEREGN', 'ORIGIN', 'HOUSEHOLD', 'UNDER15',  'EMPLOYMENT', 'AGEGROUP', 'HOUSINC', 'LIFECYCLE', 'OVER15']
UTILITY_VARIABLES = ['HOMESUPP', 'HOMESLA', 'HOMEREGN', 'ORIGIN', 'UNDER15',  'EMPLOYMENT', 'AGEGROUP', 'HOUSINC', 'LIFECYCLE', 'OVER15']

Removed_list = ['PARENT', 'GENDER']

# ORIGIN GROUP
ORIGIN_LIST = ['ORIGIN_NSW', 'ORIGIN_VIC', 'ORIGIN_QLD', 'ORIGIN_SA', 'ORIGIN_WA', 'ORIGIN_TAS', 'ORIGIN_NT', 'ORIGIN_ACT']
ORIGIN_CODE = [['1', '2'], ['3', '4'], ['5', '6'], ['7', '8'], ['9', '10'], ['11'], ['12'], ['13']]

PARENT_LIST = ['PARENT_YES', 'PARENT_NO', 'PARENT_DONT_KNOW']
PARENT_CODE = [['1'], ['0', '2'], ['9']]

YOUNGEST_LIST = ['YOUNGEST_ZERO_TO_FIVE', 'YOUNGEST_SIZX_TO_TEN', 'YOUNGEST_ELEVEN_TO_FOURTEEN', 'YOUNGEST_DONT_KNOW']
YOUNGEST_CODE = [['1'], ['3'], ['4'], ['9']]

CH15TO24_LIST = ['CH15TO24_YES', 'CH15TO24_NO', 'CH15TO24_DONT_KNOW']
CH15TO24_CODE = [['1'], ['0', '2'], ['9']]

GENDER_LIST = ['GENDER_MALE', 'GENDER_FEMALE']
GENDER_CODE = [['1'], ['2']]

MARITAL_LIST = ['MARITAL_SINGLE', 'MARITAL_COUPLE', 'MARITAL_REFUSED']
MARITAL_CODE = [['1'], ['2'], ['9']]

EMPLOYMENT_LIST = ['EMPLOYMENT_WORKING', 'EMPLOYMENT_NOT_WORKING', 'EMPLOYMENT_RETIRED', 'EMPLOYMENT_STUDYING', 'EMPLOYMENT_DONT_KNOW']
EMPLOYMENT_CODE = [['1', '2', '5'], ['3'], ['4'], ['6'], ['7', '8', '9']]

HOUSINC_LIST = ['HOUSINC_LOW', 'HOUSINC_MEDIUM', 'HOUSINC_HIGH', 'HOUSINC_DONT_KONW']
HOUSINC_CODE = [['1', '2', '3', '4', '5'], ['6', '7', '8', '9'], ['11', '12'], ['10', '13', '99', '25', '28', '29']]

LIFECYCLE_LIST = ['LIFECYCLE_SINGLE', 'LIFECYCLE_COUPLE_NO_KIDS', 'LIFECYCLE_COUPLE_WITH_KIDS', 'LIFECYCLE_DONT_KNOW']
LIFECYCLE_CODE = [['1', '2', '3', '8', '9'], ['4', '10', '11'], ['5', '6', '7'], ['0']]

AGEGROUP_LIST = ['AGEGROUP_15_29', 'AGEGROUP_30_39', 'AGEGROUP_40_49', 'AGEGROUP_50_59', 'AGEGROUP_60_69', 'AGEGROUP_70+']
AGEGROUP_CODE = [['1', '2', '3'], ['4', '5'], ['6', '7'], ['8', '9'], ['10', '11'], ['12']]

DISTANCE_DESTINATION_LIST = ['DISTANCE_TO_NSW', 'DISTANCE_TO_VIC', 'DISTANCE_TO_QLD', 'DISTANCE_TO_SA', 'DISTANCE_TO_TAS', 'DISTANCE_TO_NT']

CONSTANT_LIST = ['POPULATION_NSW', 'POPULATION_VIC', 'POPULATION_QLD', 'POPULATION_SA', 'POPULATION_TAS', 'POPULATION_NT']
# Population are in the unit of millions, such that 7.54 million people in NSW.
CONSTANT_VALUE = [0, -1.75, -2.85, -5.86, -7.02, -7.3]
# CONSTANT_BACKUP_VALUE = [7.54, 5.79, 4.69, 1.68, 0.52, 0.24]

REGION_DICT = {
    "101": "Eurobodalla Shire",
    "102": "Illawarra",
    "103": "unused",
    "104": "Sydney",
    "105": "Snowy Mountains",
    "106": "Capital Country",
    "107": "The Murray",
    "108": "Riverina",
    "109": "Dubbo",
    "110": "Hunter",
    "111": "unused",
    "112": "Nambucca Shire",
    "113": "Ballina",
    "114": "Tablelands", # "New England North West"
    "115": "Broken Hill",
    "116": "unused",
    "117": "Canberra",
    "118": "Central Coast",
    "119": "Blue Mountains",
    "120": "Lord Howe Island",
    "190": "Transit NSW",
    "198": "Sydney",
    "201": "Melbourne",
    "202": "Wimmera",
    "203": "Mallee",
    "204": "Western",
    "205": "Western Grampians",
    "206": "Bendigo Loddon",
    "207": "Peninsula",
    "208": "Central Murray",
    "209": "Goulburn",
    "210": "High Country",
    "211": "Lakes", #
    "212": "Gippsland",
    "213": "Melbourne East",
    "214": "Geelong",
    "215": "Macedon",
    "216": "Spa Country",
    "217": "Ballarat",
    "218": "Central Highlands",
    "219": "Upper Yarra",
    "220": "Murray East",
    "221": "Phillip Island",
    "290": "Transit VIC",
    "298": "Other VIC",
    "301": "Gold Coast",
    "302": "Brisbane",
    "303": "Sunshine Coast",
    "304": "Hervey Bay/Maryborough", # "Hervey Bay/Maryborough"
    "305": "unused",
    "306": "Darling Downs",
    "307": "Bundaberg",
    "308": "Fitzroy",
    "309": "Mackay",
    "310": "Whitsundays",
    "311": "Townsville",
    "312": "Tropical North Queensland",
    "313": "Great Barrier Reef",
    "314": "Outback",
    "390": "Transit QLD",
    "398": "Brisbane", # "Other QLD",
    "401": "Limestone Coast",
    "402": "Murraylands",
    "403": "Inman Valley",
    "404": "Adelaide",
    "405": "Barossa",
    "406": "Riverland",
    "407": "Sevenhill", # "Clare Valley"
    "408": "Adelaide Hills",
    "409": "Flinders Ranges",
    "410": "Outback SA",
    "411": "Eyre Peninsula",
    "412": "Yorke Peninsula",
    "413": "Kangaroo Island",
    "490": "Transit SA",
    "498": "Adelaide", # "Other SA",
    "501": "South East",
    "502": "Goldfields",
    "503": "Midwest",
    "504": "Gascoyne",
    "505": "Pilbara",
    "506": "Kimberley",
    "507": "Perth",
    "508": "Peel",
    "509": "South West",
    "510": "Great Southern",
    "511": "Wheatbelt",
    "550": "Australia's Coral Coast",
    "551": "Australia's North West",
    "552": "Australia's South West",
    "553": "Experience Perth",
    "554": "Australia's Golden Outback",
    "590": "Transit WA",
    "598": "Perth", # "Other WA"
    "601": "Hobart", # "Hobart and sourending area"
    "602": "Southern",
    "603": "East Coast",
    "604": "Northern",
    "605": "Launceston and Tamar Valley",
    "606": "North West",
    "607": "West Coast",
    "690": "Transit TAS",
    "698": "Hobart", # "Other TAS",
    "801": "Darwin",
    "802": "Kakadu",
    "803": "Arnhem",
    "804": "Katherine",
    "805": "Tablelands",
    "806": "Petermann",
    "807": "Alice Springs",
    "808": "MacDonnell",
    "809": "Daly",
    "890": "Transit NT",
    "898": "Darwin", # "Other NT",
    "900": "External Regions",
    "998": "Other Australia",
    "999": "Dont know where in Aust"
}

NSW_RANKING = {
    "Sydney": "1",
    "Central Coast": "2",
    "Eurobodalla Shire": "26",
    "Illawarra": "24",
    "Snowy Mountains": "10",
    "Capital Country": "13",
    "The Murray": "14",
    "Riverina": "15",
    "Dubbo": "12",
    "Hunter": "18",
    "Nambucca Shire": "20",
    "Ballina": "32",
    "Tablelands": "28",
    "Broken Hill": "23",
    "Canberra": "7",
    "Blue Mountains": "11",
    "Lord Howe Island": "19",
    "Transit NSW": "50",
}

VIC_RANKING = {
    "Melbourne": "1",
    "Wimmera": "15",
    "Mallee": "18",
    "Western": "31",
    "Western Grampians": "19",
    "Bendigo Loddon": "4",
    "Peninsula": "20",
    "Central Murray": "13",
    "Goulburn": "12",
    "High Country": "21",
    "Lakes": "43",
    "Gippsland": "26",
    "Melbourne East": "7",
    "Geelong": "2",
    "Macedon": "24",
    "Spa Country": "32",
    "Ballarat": "3",
    "Central Highlands": "22",
    "Upper Yarra": "34",
    "Murray East": "38",
    "Phillip Island": "39",
    "Transit VIC": "47",
    "Other VIC": "50",
}

QLD_RANKING = {
    "Brisbane": "1",
    "Gold Coast": "2",
    "Townsville": "3",
    "Great Barrier Reef": "5",
    "Sunshine Coast": "8",
    "Mackay": "9",
    "Bundaberg": "10",
    "Whitsundays": "11",
    "Hervey Bay/Maryborough": "12",
    "Tropical North Queensland": "13",
    "Darling Downs": "15",
    "Fitzroy": "22",
    "Outback": "30",
    "Transit QLD": "50",
}

SA_RANKING = {
    "Adelaide": "1",
    "Limestone Coast": "2",
    "Murraylands": "3",
    "Inman Valley": "4",
    "Barossa": "12",
    "Riverland": "15",
    "Sevenhill": "18",
    "Adelaide Hills": "21",
    "Flinders Ranges": "24",
    "Outback SA": "28",
    "Eyre Peninsula": "8",
    "Yorke Peninsula": "9",
    "Kangaroo Island": "11",
    "Transit SA": "50",
}

# WA_RANKING = {
#     ###############
#     "501": "South East",
#     "502": "Goldfields",
#     "503": "Midwest",
#     "504": "Gascoyne",
#     "505": "Pilbara",
#     "506": "Kimberley",
#     "507": "Perth",
#     "508": "Peel",
#     "509": "South West",
#     "510": "Great Southern",
#     "511": "Wheatbelt",
#     "550": "Australia's Coral Coast",
#     "551": "Australia's North West",
#     "552": "Australia's South West",
#     "553": "Experience Perth",
#     "554": "Australia's Golden Outback",
#     "590": "Transit WA",
#     "598": "Perth",  # "Other WA"
# }

TAS_RANKING = {
    "Hobart":   "1",
    "Southern": "2",
    "East Coast": "3",
    "Northern": "4",
    "Launceston and Tamar Valley": "5",
    "North West": "6",
    "West Coast": "7",
    "Transit TAS": "10",
}

NT_RANKING = {
    "Darwin": "1",
    "Alice Springs": "2",
    "Arnhem": "3",
    "Katherine": "4",
    "Tablelands": "5",
    "Petermann": "6",
    "Kakadu": "7",
    "MacDonnell": "8",
    "Daly": "9",
    "Transit NT": "10"
}