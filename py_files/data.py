
# python package
import csv


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

                # for j, item in enumerate(row):
                #     print(j, item)

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


def read_file_by_city(filename, field_list, capital_city_code, number_of_data=1000000):
    results = list()
    field_index = list()

    with open(filename, 'rb') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=',')

        for i, row in enumerate(file_reader):
            if i == 0:
                if field_list == 'ALL':
                    field_list = row

                for item in field_list:
                    field_index.append(row.index(item))

                results.append(field_list)

            elif i > number_of_data:
                break

            else:
                # TODO: need to check the capital code and change the total number of days in each the city
                row_trim = map(row.__getitem__, field_index)
                results.append(row_trim)
                # print(row_trim)
                # break

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
        for item in results:
            writer.writerow(item)

    return True









