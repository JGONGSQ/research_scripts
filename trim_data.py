#!/usr/bin/python
import csv

# Constants
## Path and File
DEFAULT_PATH = '/Users/James/Desktop/Master_Project'
TEST_OUTPUT_FILE = DEFAULT_PATH + '/Data/test_output_file.csv'
TRIAL_INPUT_DATA_FILE = DEFAULT_PATH + '/Data/data_set1_200.csv'

## Fields list
FIELD_LIST = ['ID', 'WT', 'NUMSTOP', 'stop']


def read_file(filename, field_list):
    """
        Read the source file
    :param filename: The name of the input file with its path
    :param field_list: The field would be look up
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

                for j, item in enumerate(row):
                    print(j, item)

                # first line of the file are fieldnames
                for item in field_list:
                    field_index.append(row.index(item))

                # append it to the results
                results.append(field_list)
            else:
                # get the row trim with its index number
                row_trim = map(row.__getitem__, field_index)

                # append row_trim
                results.append(row_trim)

    # return as list
    return results


def write_file(filename, results):
    """
        Write the results list to generate a new data file
    :param filename: the name of the output file with its path
    :param results: resuls in a list
    :return: None
    """

    # open the file need to be write
    with open(filename, 'w') as csvfile:
        # initial the writer
        writer = csv.writer(csvfile, delimiter=',')

        # write each row
        for item in results:
            writer.writerow(item)

    return


# read the file
results = read_file(TRIAL_INPUT_DATA_FILE, FIELD_LIST)

# write the file
write_file(TEST_OUTPUT_FILE, results)


