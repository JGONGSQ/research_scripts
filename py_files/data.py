
# python package
import csv


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
                city_data, nites_data = get_the_city_data(input_field_list, row, city_codes)

                # to see uf visited the major city
                if all(value is 0 for value in city_data) is False:

                    # initial the row for each line with all zeros
                    output_row = [0] * output_field_list.__len__()

                    # getting the value of the compulsory part
                    compulosry_data = map(row.__getitem__, map(input_field_list.index, compulsory_fields))
                    compulosry_data[0] = j
                    # getting the value of the utility parameters
                    utility_data = map(row.__getitem__, map(input_field_list.index, utility_parameters))

                    # setting the values according to the index number
                    data_set = compulosry_data + city_data + utility_data
                    map(output_row.__setitem__, map(output_field_list.index, output_field_list), data_set)

                    print(output_row)

                    results.append(output_row)
                    j += 1

    return results


def write_file(filename, results):
    """
        Write the results list to generate a new data file
    :param filename: the name of the output file with its path
    :param results: resuls in a list
    :return: True if success
    """

    # open the file need to be write
    with open(filename, 'w') as csvfile:
        # initial the writer
        writer = csv.writer(csvfile, delimiter=',')

        # write each row
        for row in results:
            writer.writerow(row)

    return True









