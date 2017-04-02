#!/usr/bin/python

# File paths
RUNNER_SMNL = 'r/run.r'
SOURCE_INPUT_FILE = '../../Data/NVS2007unit.csv'
OUTPUT_FILE = '../../Data/results/sequence.csv'
FORECAST_FILE = '../../Data/results/sequence_forecast.csv'


# Variables
ALL_VARIABLES = [
    'HOMESUPP', 'HOMESLA', 'HOMEREGN', 'ORIGIN', 'HOUSEHOLD',
    'UNDER15', 'OVER15', 'PARENT', 'YOUNGEST', 'AGEGROUP',
    'CH15TO24', 'GENDER', 'MARITAL', 'EMPLOYMENT', 'HOUSINC', 'LIFECYCLE'
]

UTILITY_VARIABLES = [
    'HOMESLA', 'ORIGIN', 'GENDER',
    'HOUSEHOLD',  'EMPLOYMENT', 'AGEGROUP', 'HOUSINC', 'LIFECYCLE',
    'OVER15'
]


STATE_LIST = ['NSW', 'VIC', 'QLD', 'SA', 'TAS', 'NT']
STATE_CODES = ['1', '2', '3', '4', '6', '8']


COMPULSORY_FIELDS = ['id', 'TOURIST_ID']
FROM_TO = ['destination', 'last_visited']

DISTANCE = ['distance']

ORIGIN_LIST = ['NSW', 'VIC', 'QLD', 'SA', 'WA', 'TAS', 'NT', 'ACT']
ORIGIN_CODE = [['1', '2'], ['3', '4'], ['5', '6'], ['7', '8'], ['9', '10'], ['11'], ['12'], ['13']]

PARENT_LIST = ['YES', 'NO', 'DONT_KNOW']
PARENT_CODE = [['1'], ['0', '2'], ['9']]

CH15TO24_LIST = ['YES', 'NO', 'DONT_KNOW']
CH15TO24_CODE = [['1'], ['0', '2'], ['9']]

GENDER_LIST = ['MALE', 'FEMALE']
GENDER_CODE = [['1'], ['2']]

MARITAL_LIST = ['SINGLE', 'COUPLE', 'REFUSED']
MARITAL_CODE = [['1'], ['2'], ['9']]

EMPLOYMENT_LIST = ['WORKING', 'NOT_WORKING', 'RETIRED', 'STUDYING', 'DONT_KNOW']
EMPLOYMENT_CODE = [['1', '2', '5'], ['3'], ['4'], ['6'], ['7', '8', '9']]

HOUSINC_LIST = ['LOW', 'MEDIUM', 'HIGH', 'DONT_KONW']
HOUSINC_CODE = [['1', '2', '3', '4', '5'], ['6', '7', '8', '9'], ['11', '12'], ['10', '13', '99', '25', '28', '29']]

LIFECYCLE_LIST = ['SINGLE', 'COUPLE_NO_KIDS', 'COUPLE_WITH_KIDS', 'DONT_KNOW']
LIFECYCLE_CODE = [['1', '2', '3', '8', '9'], ['4', '10', '11'], ['5', '6', '7'], ['0']]

AGEGROUP_LIST = ['15_29', '30_39', '40_49', '50_59', '60_69', '70+']
AGEGROUP_CODE = [['1', '2', '3'], ['4', '5'], ['6', '7'], ['8', '9'], ['10', '11'], ['12']]