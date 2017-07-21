#!/usr/bin/python


# File paths
SOURCE_INPUT_FILE = '../../Data/NVS2007unit.csv'
OUTPUT_FILE = '../../Data/results/conditional_mnl.csv'
FORECAST_FILE = '../../Data/results/conditional_forecast.csv'
REGN_CODE_DICT_PATH_V2 = '../../Data/regn_code_dict_v2.csv'

UTILITY_VARIABLES = [
    'HOMESLA', 'HOMEREGN', 'GENDER',
    'HOUSEHOLD', 'EMPLOYMENT', 'AGEGROUP', 'HOUSINC', 'LIFECYCLE',
    'OVER15'
]

COMPULSORY_FIELDS = ['TOURIST_ID']
ALTERNATIVE_CATEGORY = ['choice_situation', 'mode_id', 'choice']

STATE_LIST = ['NSW', 'VIC', 'QLD', 'SA', 'TAS', 'NT']
STATE_CODES = ['1', '2', '3', '4', '6', '8']
STATE_ALTERNATIVES = ['1', '2', '3', '4', '5', '6']

ORIGIN_LIST = ['ORIGIN_NSW', 'ORIGIN_VIC', 'ORIGIN_QLD', 'ORIGIN_SA', 'ORIGIN_WA', 'ORIGIN_TAS', 'ORIGIN_NT',
               'ORIGIN_ACT']
ORIGIN_CATEGORY = ['1', '2', '3', '4', '5', '6', '7', '8']
ORIGIN_CODE = [['1', '2'], ['3', '4'], ['5', '6'], ['7', '8'], ['9', '10'], ['11'], ['12'], ['13']]

PARENT_LIST = ['PARENT_YES', 'PARENT_NO', 'PARENT_DONT_KNOW']
PARENT_CATEGORY = ['1', '2', '3']
PARENT_CODE = [['1'], ['0', '2'], ['9']]

CH15TO24_LIST = ['CH15TO24_YES', 'CH15TO24_NO', 'CH15TO24_DONT_KNOW']
CH15TO24_CATEGORY = ['1', '2', '3']
CH15TO24_CODE = [['1'], ['0', '2'], ['9']]

GENDER_LIST = ['GENDER_MALE', 'GENDER_FEMALE']
GENDER_CATEGORY = ['1', '2']
GENDER_CODE = [['1'], ['2']]

MARITAL_LIST = ['MARITAL_SINGLE', 'MARITAL_COUPLE', 'MARITAL_REFUSED']
MARITAL_CATEGORY = ['1', '2', '3']
MARITAL_CODE = [['1'], ['2'], ['9']]

EMPLOYMENT_LIST = ['EMPLOYMENT_WORKING', 'EMPLOYMENT_NOT_WORKING', 'EMPLOYMENT_RETIRED', 'EMPLOYMENT_STUDYING',
                   'EMPLOYMENT_DONT_KNOW']
EMPLOYMENT_CATEGORY = ['1', '2', '3', '4', '5']
EMPLOYMENT_CODE = [['1', '2', '5'], ['3'], ['4'], ['6'], ['7', '8', '9']]

HOUSINC_LIST = ['HOUSINC_LOW', 'HOUSINC_MEDIUM', 'HOUSINC_HIGH', 'HOUSINC_DONT_KONW']
HOUSINC_CATEGORY = ['1', '2', '3', '4']
HOUSINC_CODE = [['1', '2', '3', '4', '5'], ['6', '7', '8', '9'], ['11', '12'], ['10', '13', '99', '25', '28', '29']]

LIFECYCLE_LIST = ['LIFECYCLE_SINGLE', 'LIFECYCLE_COUPLE_NO_KIDS', 'LIFECYCLE_COUPLE_WITH_KIDS', 'LIFECYCLE_DONT_KNOW']
LIFECYCLE_CATEGORY = ['1', '2', '3', '4']
LIFECYCLE_CODE = [['1', '2', '3', '8', '9'], ['4', '10', '11'], ['5', '6', '7'], ['0']]

AGEGROUP_LIST = ['AGEGROUP_15_29', 'AGEGROUP_30_39', 'AGEGROUP_40_49', 'AGEGROUP_50_59', 'AGEGROUP_60_69',
                 'AGEGROUP_70+']
AGEGROUP_CATEGORY = ['1', '2', '3', '4', '5', '6']
AGEGROUP_CODE = [['1', '2', '3'], ['4', '5'], ['6', '7'], ['8', '9'], ['10', '11'], ['12']]
