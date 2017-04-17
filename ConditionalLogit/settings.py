#!/usr/bin/python


# File paths
SOURCE_INPUT_FILE = '../../Data/NVS2007unit.csv'
OUTPUT_FILE = '../../Data/results/conditional_mnl.csv'
FORECAST_FILE = '../../Data/results/conditional_forecast.csv'





UTILITY_VARIABLES = [
    'HOMESLA', 'ORIGIN', 'GENDER',
    'HOUSEHOLD',  'EMPLOYMENT', 'AGEGROUP', 'HOUSINC', 'LIFECYCLE',
    'OVER15'
]

COMPULSORY_FIELDS = ['id', 'TOURIST_ID']

STATE_LIST = ['NSW', 'VIC', 'QLD', 'SA', 'TAS', 'NT']
STATE_CODES = ['1', '2', '3', '4', '6', '8']
STATE_ALTERNATIVES = ['1', '2', '3', '4', '5', '6']
