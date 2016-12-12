
# python package
import csv
import os
from settings import *


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
    order_data = ''
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
            city_name = CITY_LISTS.__getitem__(city_codes.index(location))
            if order_data == '':
                order_data += city_name
            else:
                order_data = order_data + '-' + city_name

    print(order_data)
    return city_data, order_data


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
    # print("### This is the value in the line:", value)
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


def write_file(filename, data):
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

    if case_config == 1:
        list_of_variables = list(set(ALL_VARIABLES).difference(set(EXECLUDE_VARIABLE_1)))

    if case_config == 4:
        list_of_variables = list(set(ALL_VARIABLES).difference(set(EXECLUDE_VARIABLE_4)))

    if case_config == 7:
        list_of_variables = list(set(ALL_VARIABLES).difference(set(EXECLUDE_VARIABLE_7)))

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

    with open(input_file, 'rb') as input_csv:
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

                    # temp_number = city_data.__len__() - 2
                    # print('####', count_zero(city_data), temp_number)

                    # if temp_number >= count_zero(data):
                    if all(value is 0 for value in city_data) is False:

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
    is_successful = write_file(filename=output_file, data=data)
    return is_successful


def read_combinations(input_file, output_file, compulsory_fields, city_lists, city_codes, number_of_data=40000):
    input_field_list = None
    index_number = 1
    data = list()
    output_fields_list = compulsory_fields + city_lists

    data.append(output_fields_list)
    with open(input_file, 'rb') as input_csv:
        file_reader = csv.reader(input_csv, delimiter=',')

        for i , row in enumerate(file_reader):
            if i == 0:
                input_field_list = row
            elif i > number_of_data:
                break
            else:

                city_data, order_data = get_the_city_data_in_orders(input_field_list, row, city_codes)

                if all(value is 0 for value in city_data) is False:
                    output_row = [0] * output_fields_list.__len__()
                    compulsory_data = map(row.__getitem__, map(input_field_list.index, compulsory_fields))
                    compulsory_data[0] = index_number
                    compulsory_data[3] = order_data

                    data_set = compulsory_data + city_data
                    map(output_row.__setitem__, map(output_fields_list.index, output_fields_list), data_set)
                    print(output_row)
                    data.append(output_row)
                    index_number += 1

    is_successful = write_file(filename=output_file, data=data)
    return is_successful
