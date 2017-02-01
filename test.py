#!/usr/bin/python

# Import the packagess
from py_files.data import cal_distance


origin_code = "NSW"
destination_code = "VIC"

distance = cal_distance(origin_code, destination_code)
print('Distance between {origin} and {destination}'.format(origin=origin_code, destination=destination_code))
print(distance)
