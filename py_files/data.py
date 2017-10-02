
# python package
import csv
import os
import numpy as np

from mdcev.settings import *
from settings import *
from geopy.geocoders import Nominatim
from geopy.distance import vincenty, great_circle


def count_on_pure_data(pure_data, number_of_alternatives):
    # initial the matrix
    duration_counts = np.zeros(number_of_alternatives)
    alternative_counts = np.zeros(number_of_alternatives)
    number_of_chosen_alternative_counts = np.zeros(number_of_alternatives)

    # add the value to the matrix line by line
    for row in pure_data:
        # Get the duration value
        temp_a = np.asarray(row)
        duration_counts = np.add(temp_a, duration_counts)
        # Get the hit value
        temp_b = np.nonzero(row)
        for index in temp_b[0]:
            alternative_counts[index] += 1
        # Get the number of chosen alternatives in the matrix
        temp_c = np.count_nonzero(row)
        number_of_chosen_alternative_counts[temp_c - 1] += 1

    return duration_counts, alternative_counts, number_of_chosen_alternative_counts


def update_regn_dict():
    geolocator = Nominatim()
    data = list()
    head_row = ['key', 'location', 'latitude', 'longitude']
    data.append(head_row)

    for item in REGION_DICT:
        key = item.__str__()
        location_address, state = get_code_address(key)
        latitude = None
        longitude = None

        try:
            destination = geolocator.geocode(location_address)
        except Exception:
            print ("Destination is None")
            destination = None

        if destination:
            latitude = destination.latitude
            longitude = destination.longitude

        data.append([key, location_address, latitude, longitude])

    return data


def get_pure_data(data, index):
    pure_data = list()
    for i, row in enumerate(data):
        if i == 0:
            pass
        else:
            temp_row = map(row.__getitem__, index)
            temp_row = map(float, temp_row)
            pure_data.append(temp_row)
    return pure_data


def get_regn_dict(filepath):
    regn_dict = {}

    with open(filepath, 'rU') as input_csv:
        file_reader = csv.reader(input_csv, delimiter=',')
        for i, row in enumerate(file_reader):
            key = row[0]
            latitude = row[2]
            longitude = row[3]
            regn_dict[key] = {
                "latitude": latitude,
                "longitude": longitude
            }

    return regn_dict


def get_coefficient_dict(filepath):
    coefficient_dict = {}

    with open(filepath, 'rU') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=',')
        # initial values
        writing_flag = False
        alternative_counter = 1
        variable_counter = 1

        # read line by line
        for row in file_reader:
            if row[0] == "uno":
                writing_flag = True
                alternative_counter += 1
                variable_counter = 0
                alternative_name = "alternative_{alternative_counter}".format(alternative_counter=alternative_counter)
                coefficient_dict.update({alternative_name: {}})

            variable_counter += 1
            variable_name = "variable_{variable_counter}".format(variable_counter=variable_counter)

            if row[0] == "sigm":
                writing_flag = False

            if writing_flag:
                # print(alternative_name, variable_name, row)
                coefficient_dict[alternative_name].update({
                    variable_name: {
                        "name": row[0],
                        "value": float(row[1])
                    }
                })

    return coefficient_dict


def get_ranking_dict(state):
    ranking_dict = None

    if state == "NSW" or state == "New South Wales":
        ranking_dict = NSW_RANKING
    elif state == "SA" or state == "South Australia":
        ranking_dict = SA_RANKING
    elif state == "VIC" or state == "Victoria":
        ranking_dict = VIC_RANKING
    elif state == "QLD" or state == "Queensland":
        ranking_dict = QLD_RANKING
    elif state == "TAS" or state == "Tasmania":
        ranking_dict = TAS_RANKING
    elif state == "NT" or state == "Northern Territory":
        ranking_dict = NT_RANKING

    return ranking_dict


# def cal_distance(origin_name, destination_name):
#     """
#         Calculate the distance between points
#     :param origin_name: such as 'TAS', 'NSW' or 'TAS'
#     :param destination_name: same as origin code
#     :return: distance between two point in km
#     """
#     # initial the package
#     geolocator = Nominatim()
#
#     # get the origin code
#     try:
#         origin = geolocator.geocode(origin_name, timeout=10)
#
#     # get destination
#         destination = geolocator.geocode(destination_name, timeout=10)
#     except Exception:
#         return 0
#     # make the points
#     from_origin = (origin.latitude, origin.longitude)
#     to_destination = (destination.latitude, destination.longitude)
#     print(from_origin, to_destination)
#
#     distance = vincenty(from_origin, to_destination).km
#
#     # round the distance to the closest km
#     return int(distance)

def cal_distance_v2(point_1, point_2):
    """
        Calculate the distance between points
    :param origin_name: such as 'TAS', 'NSW' or 'TAS'
    :param destination_name: same as origin code
    :return: distance between two point in km
    """

    # make the points
    from_origin = (point_1["latitude"], point_1["longitude"])
    to_destination = (point_2["latitude"], point_2["longitude"])
    print(from_origin, to_destination)

    distance = vincenty(from_origin, to_destination).km

    # round the distance to the closest km
    return int(distance)


def find_index_in_list(list, value):
    index = None
    for i, sub_list in enumerate(list):
        for item in sub_list:
            if item == value:
                index = i
    return index


def get_the_city_data(input_field_list, row, city_codes):
    """
    :param input_field_list: the first line of the input file
    :param row: data for each line
    :param city_codes: capital city codes
    :return: binary matrix if the person visited the capital city
    """
    city_data = [0] * city_codes.__len__()
    nites_data = [0] * city_codes.__len__()
    # need to be careful here to get the total number of stops
    number_of_stops = row.__getitem__(input_field_list.index('NUMSTOP'))

    # for each stop do the check
    for i in range(int(number_of_stops)):
        location = row.__getitem__(input_field_list.index('REGN%s' % str(i + 1)))
        # print(location)
        if location in city_codes:
            # city_data.__setitem__(city_codes.index(location), 1)

            # get the nites data, the number of days in the city
            nites = row.__getitem__(input_field_list.index('NITES%s' % str(i + 1)))
            nites_data.__setitem__(city_codes.index(location), int(nites))
            city_data.__setitem__(city_codes.index(location), int(nites))

    # print(city_data)
    return city_data, nites_data


def get_the_city_data_in_orders(input_field_list, row, city_codes):
    """
    :param input_field_list: the first line of the input file
    :param row: data for each line
    :param city_codes: capital city codes
    :return: binary matrix if the person visited the capital city
    """
    city_data = [0] * city_codes.__len__()
    nites_data = [0] * city_codes.__len__()
    # need to be careful here to get the total number of stops
    number_of_stops = row.__getitem__(input_field_list.index('NUMSTOP'))
    path = ''
    # for each stop do the check
    for i in range(int(number_of_stops)):
        location = row.__getitem__(input_field_list.index('REGN%s' % str(i + 1)))
        # print(location)
        if location in city_codes:
            # city_data.__setitem__(city_codes.index(location), 1)

            # get the nites data, the number of days in the city
            nites = row.__getitem__(input_field_list.index('NITES%s' % str(i + 1)))
            nites_data[city_codes.index(location)] += int(nites)
            city_data[city_codes.index(location)] += int(nites)
            city_name = CITY_LISTS.__getitem__(city_codes.index(location))
            path = generate_path(path, city_name)

    print(path)
    return city_data, path


def get_state_location(location):
    state_location = location[0]
    return state_location


def get_code_address(region_code):
    city = REGION_DICT[region_code]
    state_code = get_state_location(region_code)

    if state_code not in STATE_CODES:
        return None, None
    state = STATE_FULL[STATE_CODES.index(state_code)]

    address = city + ", " + state

    # print("This is the address", address)

    return address, state


def generate_path(path, location_name):
    if path.endswith(location_name) is False:
        if path == '':
            path += location_name
        else:
            path = path + '-' + location_name
    return path


def get_the_state_data(input_field_list, row, state_codes):
    state_data = [0] * state_codes.__len__()
    nites_data = [0] * state_codes.__len__()

    number_of_stops = row.__getitem__(input_field_list.index('NUMSTOP'))
    path = ''

    for i in range(int(number_of_stops)):
        location = row.__getitem__(input_field_list.index('REGN%s' % str(i + 1)))
        state_location = get_state_location(location)

        if state_location in state_codes:
            nites = row.__getitem__(input_field_list.index('NITES%s' % str(i + 1)))
            nites_data[state_codes.index(state_location)] += int(nites)
            state_data[state_codes.index(state_location)] += int(nites)
            state_name = STATE_LISTS.__getitem__(state_codes.index(state_location))

            path = generate_path(path, state_name)

    return state_data, path


def initial_distance_data(regn_dict, home_point, distance_destination_list):
    # initial the data with zeros
    distance_data = [0] * distance_destination_list.__len__()

    # calculate the distance to capital city of each state
    for i, code in enumerate(CITY_CODES):
        # Calculate the state
        distance = cal_distance_v2(home_point, regn_dict[code])
        distance_data[i] = distance

    return distance_data


def get_distance_data(input_field_list, distance_destination_list, state_list, row):
    # initial the list
    regn_dict = get_regn_dict(REGN_CODE_DICT_PATH_V2)
    # distance_data = [0] * distance_destination_list.__len__()
    distance_ranking = [100] * distance_destination_list.__len__()

    number_of_stops = row.__getitem__(input_field_list.index('NUMSTOP'))

    home_location_code = row.__getitem__(input_field_list.index('HOMEREGN'))
    home_address, home_state = get_code_address(home_location_code)

    # initial the distance data
    distance_data = initial_distance_data(regn_dict, regn_dict[home_location_code], distance_destination_list)

    if home_address is None:
        # print("Home address is None, not in the state list")
        return distance_data

    for i in range(int(number_of_stops)):
        # get the destination code
        destination_location_code = row.__getitem__(input_field_list.index('REGN%s' % str(i + 1)))
        # get the destination address and its state
        destination_address, state = get_code_address(destination_location_code)
        # get the ranking dictionary of the table
        if state:
            ranking = get_ranking_dict(state)
            ranking_order = ranking[REGION_DICT[destination_location_code]]
            index = STATE_FULL.index(state)
            # print("########", int(ranking_order), index)

            if distance_ranking[index] >= int(ranking_order):
                distance = cal_distance_v2(regn_dict[home_location_code], regn_dict[destination_location_code])
                distance_data[index] = distance
                distance_ranking[index] = ranking_order
                # print("Distance: %s km" % distance)


    # print('This is the distance data', distance_data)
    # print(row)
    # print(input_field_list)
    # print('State List:', state_list)
    # raise Exception

    return distance_data


def get_the_utility_variable_data(input_field_list, row, variable, variable_codes):
    """
    :param input_field_list:
    :param row:
    :param variable:
    :param variable_codes:
    :return:
    """
    variable_data = [0] * variable_codes.__len__()
    value = row.__getitem__(input_field_list.index(variable))
    print("### This is the value in the line:", value, variable)
    if value:
        variable_data.__setitem__(find_index_in_list(list=variable_codes, value=value), 1)

    return variable_data


def read_file(filename, field_list, number_of_data=1000000):
    """
        Read the source file
    :param filename: The name of the input file with its path
    :param field_list: The field would be look up
    :param number_of_data: the total number of data needed for computation, if not given, would be 1,000,000 as default
    :return: results list
    """
    # initial the list
    results = list()
    field_index = list()

    # open the file need to be read
    with open(filename, 'rb') as csvfile:

        # initial the reader
        file_reader = csv.reader(csvfile, delimiter=',')

        # looping each row
        for i, row in enumerate(file_reader):
            if i == 0:

                # first line of the file are fieldnames
                for item in field_list:
                    field_index.append(row.index(item))

                # append it to the results
                results.append(field_list)

            elif i > number_of_data:
                break

            else:
                # get the row trim with its index number
                row_trim = map(row.__getitem__, field_index)

                # append row_trim
                results.append(row_trim)

    # return as list
    return results


def read_file_by_city(filename, compulsory_fields, city_lists, city_codes, utility_parameters, number_of_data=1000000):
    """
    :param filename: the input file name as path
    :param compulsory_fields: example in the settings file, should be list of fileds
    :param city_lists: list of city names
    :param city_codes: list of city codes
    :param utility_parameters: list of utility parameters for the model
    :param number_of_data: maximum number going to read, if not given, would be 1 million.
    :return: results as list
    """
    print utility_parameters
    results = list()
    output_field_list = compulsory_fields + city_lists + utility_parameters
    input_field_list = None
    j = 1
    with open(filename, 'rb') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=',')

        for i, row in enumerate(file_reader):
            if i == 0:
                input_field_list = row
                # print(output_field_list)
                results.append(output_field_list)

            elif i > number_of_data:
                break

            else:
                # getting the value of the utility parameters
                utility_data = map(row.__getitem__, map(input_field_list.index, utility_parameters))

                # To check the utility data is empty or not
                if ' ' not in utility_data:

                    city_data, nites_data = get_the_city_data(input_field_list, row, city_codes)

                    # to see uf visited the major city
                    if all(value is 0 for value in city_data) is False:

                        # initial the row for each line with all zeros
                        output_row = [0] * output_field_list.__len__()

                        # getting the value of the compulsory part
                        compulosry_data = map(row.__getitem__, map(input_field_list.index, compulsory_fields))
                        compulosry_data[0] = j

                        # setting the values according to the index number
                        data_set = compulosry_data + city_data + utility_data
                        map(output_row.__setitem__, map(output_field_list.index, output_field_list), data_set)

                        print(output_row)

                        results.append(output_row)
                        j += 1

    return results


def write_data_to_csv(filename, data):
    """
        Write the results list to generate a new data file
    :param filename: the name of the output file with its path
    :param data: its a two-dimensional array
    :return: True if success
    """

    # open the file need to be write
    with open(filename, 'w') as csvfile:
        # initial the writer
        writer = csv.writer(csvfile, delimiter=',')

        # write each row
        for row in data:
            writer.writerow(row)

    return True


def read_csv_to_data(filename):

    data = list()

    with open(filename, 'rU') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=',')

        for row in file_reader:
            data.append(row)

    return data


def convert_txt_to_csv(filepath):
    """
        Convert the txt file to csv file.
    :param filepath: the path of the input file
    :return:
    """

    output_file = filepath.replace('.txt', '.csv')

    with open(output_file, 'wb') as csvfile:
        row_writer = csv.writer(csvfile, delimiter=',')
        file = open(filepath, 'r')

        for line in file:
            row = filter(None, line.split(' '))
            row_writer.writerow(row)

    return output_file


def convert_list_to_str(input_list):
    output_string = ''

    for i, item in enumerate(input_list):
        output_string = output_string + item
        if i != len(input_list) - 1:
            output_string += ','

    return output_string


def convert_tuple_to_list(tuple_object):
    list_object = list()

    for item in tuple_object:
        list_object.append(item)

    return list_object


def case_config_excluding_variables(case_config):
    list_of_variables = ALL_VARIABLES

    # if case_config == 1:
    #     list_of_variables = list(set(ALL_VARIABLES).difference(set(EXECLUDE_VARIABLE_1)))
    #
    # if case_config == 4:
    #     list_of_variables = list(set(ALL_VARIABLES).difference(set(EXECLUDE_VARIABLE_4)))
    #
    # if case_config == 7:
    #     list_of_variables = list(set(ALL_VARIABLES).difference(set(EXECLUDE_VARIABLE_7)))

    return list_of_variables


def filter_files(dirpath):
    files = os.listdir(dirpath)

    for file in files:
        if os.path.isdir(dirpath + '/' + file):
            pass
        else:
            if is_file_converge(dirpath + '/' + file):
                os.rename(dirpath + '/' + file, dirpath + '/converge/' + file)
            else:
                os.rename(dirpath + '/' + file, dirpath + '/notconverge/' + file)
    return


def get_utility_variables(alternatives):
    utility_variable = list()

    # in each alternative may have the different variable
    for alternative in alternatives:

        for item in alternative:
            if item not in utility_variable:
                utility_variable.append(item)

    return utility_variable


def is_file_converge(filepath):
    try:
        with open(filepath, 'r') as fp:
            if 'Inf' in fp.read():
                return False
            else:
                return True
    except Exception:
        return False


def get_utility_parameters_list(utility_parameters):
    utility_parameters_list = list()

    for variable in utility_parameters:

        variable_list = get_the_vairable_list(variable)
        if variable_list:
            utility_parameters_list += variable_list
        else:
            utility_parameters_list.append(variable)

    return utility_parameters_list


def get_utility_parameters_value(input_field_list, utility_parameters, row):
    value_list = list()
    # print utility_parameters
    for variable in utility_parameters:
        variable_codes = get_the_variable_codes(variable)
        # print variable
        if variable_codes:
            variable_data = get_the_utility_variable_data(
                input_field_list=input_field_list,
                row=row,
                variable=variable,
                variable_codes=variable_codes
            )
            value_list += variable_data
        else:
            # print input_field_list.index(variable)
            value_list.append(row.__getitem__(int(input_field_list.index(variable))))

    return value_list


def get_the_variable_codes(variable):
    variable_codes = None

    if variable == 'ORIGIN':
        variable_codes = ORIGIN_CODE

    elif variable == 'PARENT':
        variable_codes = PARENT_CODE

    elif variable == 'YOUNGEST':
        variable_codes = YOUNGEST_CODE

    elif variable == "GENDER":
        variable_codes = GENDER_CODE

    elif variable == 'MARITAL':
        variable_codes = MARITAL_CODE

    elif variable == 'EMPLOYMENT':
        variable_codes = EMPLOYMENT_CODE

    elif variable == 'HOUSINC':
        variable_codes = HOUSINC_CODE

    elif variable == 'LIFECYCLE':
        variable_codes = LIFECYCLE_CODE

    elif variable == 'AGEGROUP':
        variable_codes = AGEGROUP_CODE

    elif variable == 'PARTYPE':
        variable_codes = PARTYPE_CODE

    elif variable == 'GROUPTYPE':
        variable_codes = GROUPTYPE_CODE

    elif variable == 'TRIP_PURPOSE':
        variable_codes = TRIP_PURPOSE_CODE

    elif variable == 'CUSTOMS':
        variable_codes = CUSTOMS_CODE

    return variable_codes


def get_the_vairable_list(variable):
    variable_list = None
    if variable == 'ORIGIN':
        variable_list = ORIGIN_LIST

    elif variable == 'PARENT':
        variable_list = PARENT_LIST

    elif variable == 'YOUNGEST':
        variable_list = YOUNGEST_LIST

    elif variable == "GENDER":
        variable_list = GENDER_LIST

    elif variable == 'MARITAL':
        variable_list = MARITAL_LIST

    elif variable == 'EMPLOYMENT':
        variable_list = EMPLOYMENT_LIST

    elif variable == 'HOUSINC':
        variable_list = HOUSINC_LIST

    elif variable == 'LIFECYCLE':
        variable_list = LIFECYCLE_LIST

    elif variable == 'AGEGROUP':
        variable_list = AGEGROUP_LIST

    elif variable == 'PARTYPE':
        variable_list = PARTYPE_LIST

    elif variable == 'GROUPTYPE':
        variable_list = GROUPTYPE_LIST

    elif variable == 'TRIP_PURPOSE':
        variable_list = TRIP_PURPOSE_LIST

    elif variable == 'CUSTOMS':
        variable_list = CUSTOMS_LIST

    return variable_list


def count_zero(data):
    count = 0
    for item in data:
        if item == 0:
            count += 1
    return count


def trim_data(input_file, output_file, compulsory_fields, city_lists, city_codes, utility_parameters, number_of_data=40000):
    """
    :param input_file: the path of the input file
    :param output_file: the path of the output file
    :param compulsory_fields: compulsory fields for the R package
    :param city_lists: list of city names
    :param city_codes: list tof city codes
    :param utility_parameters: list of utility parameters for the model
    :param number_of_data: maximum number of data going to be read, if not givem the default value is 2000
    :return: Boolean value
    """
    print utility_parameters
    # initials
    data = list()
    input_field_list = None
    index_number = 1

    utility_parameters_list = get_utility_parameters_list(utility_parameters)
    output_fields_list = compulsory_fields + city_lists + utility_parameters_list

    # append headings here
    data.append(output_fields_list)

    with open(input_file, 'rU') as input_csv:
        file_reader = csv.reader(input_csv, delimiter=',')

        # process the data line by line
        for i, row in enumerate(file_reader):
            if i == 0:
                input_field_list = row

            elif i > number_of_data:
                break
            else:
                # getting the value of the utility parameters
                utility_data = map(row.__getitem__, map(input_field_list.index, utility_parameters))

                if ' ' not in utility_data:
                    city_data, nites_data = get_the_city_data(input_field_list, row, city_codes)

                    # if city_data.__len__() - 1 == count_zero(city_data):
                    if city_data.__len__() - 2 >= count_zero(city_data):
                    # if all(value is 0 for value in city_data) is False:


                        # initial the row for each line with all zeros
                        output_row = [0] * output_fields_list.__len__()

                        # getting the value of the compulsory part
                        compulsory_data = map(row.__getitem__, map(input_field_list.index, compulsory_fields))
                        compulsory_data[0] = index_number

                        # getting the utility parameters data according to the utility parameters
                        utility_variable_data = get_utility_parameters_value(input_field_list, utility_parameters, row)

                        # setting the values according to the index number
                        data_set = compulsory_data + city_data + utility_variable_data
                        map(output_row.__setitem__, map(output_fields_list.index, output_fields_list), data_set)

                        print(output_row)
                        data.append(output_row)
                        index_number += 1

    # write the data to the output file
    is_successful = write_data_to_csv(filename=output_file, data=data)
    return is_successful


def read_state_combinations(input_file, output_file, compulsory_fields, state_list, state_codes, utility_parameters, distance_destination_list, number_of_data=40000):

    # print utility_parameters
    # initials
    input_field_list = None
    index_number = 1
    data = list()
    total_duration = ["Duration"]

    # make the title
    utility_parameters_list = get_utility_parameters_list(utility_parameters)
    output_fields_list = compulsory_fields + state_list + utility_parameters_list + distance_destination_list + CONSTANT_LIST + total_duration

    # append the title
    data.append(output_fields_list)

    with open(input_file, 'rU') as input_csv:
        file_reader = csv.reader(input_csv, delimiter=',')

        for i, row in enumerate(file_reader):
            if i == 0:
                input_field_list = row
            elif i > number_of_data:
                break
            else:
                # getting the value of the utility parameters
                utility_data = map(row.__getitem__, map(input_field_list.index, utility_parameters))
                if ' ' not in utility_data:

                    state_data, order_data = get_the_state_data(input_field_list, row, state_codes)

                    # if state_data.__len__() - 1 == count_zero(state_data):
                    # if state_data.__len__() - 2 >= count_zero(state_data):
                    if all(value is 0 for value in state_data) is False:
                        output_row = [0] * output_fields_list.__len__()
                        compulsory_data = map(row.__getitem__, map(input_field_list.index, compulsory_fields))
                        compulsory_data[0] = index_number
                        compulsory_data[3] = order_data
                        print('This is the state data line', state_data, sum(state_data))
                        # getting the utility parameters data according to the utility parameters
                        utility_variable_data = get_utility_parameters_value(input_field_list, utility_parameters, row)
                        distance_data = get_distance_data(input_field_list, distance_destination_list, state_list, row)

                        data_set = compulsory_data + state_data + utility_variable_data \
                                   + distance_data + CONSTANT_VALUE + [sum(state_data)]
                        map(output_row.__setitem__, map(output_fields_list.index, output_fields_list), data_set)

                        # print(output_row)
                        data.append(output_row)
                        index_number += 1

    is_successful = write_data_to_csv(filename=output_file, data=data)
    return is_successful


def read_ivs_state_combinations(input_file, output_file, compulsory_fields, state_list, state_codes, utility_parameters, distance_destination_list, number_of_data=40000):

    input_field_list = None
    index_number = 1
    data = list()
    total_duration = ["Duration"]

    utility_parameters_list = get_utility_parameters_list(utility_parameters)

    # print(utility_parameters_list)
    # output_fields_list = compulsory_fields + state_list + utility_parameters_list + distance_destination_list + CONSTANT_LIST + total_duration
    output_fields_list = compulsory_fields + state_list + utility_parameters_list + CONSTANT_LIST + total_duration
    data.append(output_fields_list)
    data_count = 0

    with open(input_file, 'rU') as input_csv:
        file_reader = csv.reader(input_csv, delimiter=',')

        for i, row in enumerate(file_reader):
            if i == 0:
                input_field_list = row
            elif i > number_of_data:
                break
            else:
                # getting the value of the utility parameters
                utility_data = map(row.__getitem__, map(input_field_list.index, utility_parameters))
                # if ' ' not in utility_data:
                if not any(item in [' ', 'NA'] for item in utility_data):
                    data_count += 1
                    state_data, order_data = get_the_state_data(input_field_list, row, state_codes)

                    # if state_data.__len__() - 1 == count_zero(state_data):
                    # if state_data.__len__() - 2 >= count_zero(state_data):
                    if all(value is 0 for value in state_data) is False:

                        output_row = [0] * output_fields_list.__len__()
                        compulsory_data = map(row.__getitem__, map(input_field_list.index, compulsory_fields))
                        compulsory_data[0] = index_number
                        compulsory_data[4] = order_data
                        print('This is the state data line', state_data, sum(state_data))
                        # getting the utility parameters data according to the utility parameters
                        utility_variable_data = get_utility_parameters_value(input_field_list, utility_parameters, row)
                        # distance_data = get_distance_data(input_field_list, distance_destination_list, state_list, row)

                        # data_set = compulsory_data + state_data + utility_variable_data \
                        #            + distance_data + CONSTANT_VALUE + [sum(state_data)]
                        data_set = compulsory_data + state_data + utility_variable_data + CONSTANT_VALUE + [sum(state_data)]
                        map(output_row.__setitem__, map(output_fields_list.index, output_fields_list), data_set)

                        # print(output_row)
                        data.append(output_row)
                        index_number += 1

    is_successful = write_data_to_csv(filename=output_file, data=data)
    print("This is total number of filtered data", data_count)
    return is_successful

