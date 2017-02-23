#!/usr/bin/python

# Import the packagess
from py_files.data import get_code_address, update_regn_dict, write_file, get_regn_dict
from py_files.settings import *
from py_files.forecast import evaluate_forcasting
from geopy.geocoders import Nominatim


# geolocator = Nominatim()
#
# origin_code = "Lakes, Victoria"
# destination_code = "Sydney, New South Wales"
#
# destination = geolocator.geocode(origin_code)
# print destination, destination.latitude, destination.longitude


# distance = cal_distance(origin_code, destination_code)
# print('Distance between {origin} and {destination}'.format(origin=origin_code, destination=destination_code))
# print(distance)


# for item in REGION_DICT:
#     address, state = get_code_address(item.__str__())
#     try:
#         destination = geolocator.geocode(address)
#     except Exception:
#         destination = None
#     if destination is None:
#         print address
#
# data = update_regn_dict()
# write_file(filename=REGN_CODE_DICT_PATH, data=data)

# regn_dict = get_regn_dict(REGN_CODE_DICT_PATH_V2)
# print(regn_dict['104'])

data_filepath = INPUT_DIR_PATH + '/NVS2007_trimed_v3.csv'
results_file = RESULTS_PATH + '/results' + '_{}'.format(1) + '_{}'.format('MDCEV_forecasting') + '.csv'

evaluate_forcasting(data_file=data_filepath, result_file=results_file, alternative_list=STATE_LISTS)

