#!/usr/bin/python

# Import the packagess
from py_files.data import cal_distance

from geopy.geocoders import Nominatim


origin_code = "Capital Country, New South Wales"
destination_code = "Limestone Coast, South Australia"

distance = cal_distance(origin_code, destination_code)
print('Distance between {origin} and {destination}'.format(origin=origin_code, destination=destination_code))
print(distance)


# geolocator = Nominatim()
# destination = geolocator.geocode(origin_code)
# print destination