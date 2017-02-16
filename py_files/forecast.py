#!/usr/bin/python
import csv


def get_coef_file(filepath):
    data = list()

    with open(filepath, 'rU') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=',')
        # initial values
        variable_flag = False
        variables = None
        values = None
        alternative_counter = 0
        variable_counter = 0
        data.append(['variables', 'values'])

        # read line by line
        for row in file_reader:
            if row[0] == "uno":
                if alternative_counter != 0:
                    data.append([variables, values])
                variables = ''
                values = ''
                variable_flag = True
                variable_counter = 0
                alternative_counter += 1

            variable_counter += 1

            # if row[0] == "sigm":
            #     variable_flag = False

            if row[0] == 'D1' or row[0] == 'G1':
                data.append([variables, values])
                variable_flag = False
                variables = 'end'
                values = 'end'

            if variable_flag:
                if variable_counter == 1:
                    variables = variables + row[0]
                    values = values + str(float(row[1]))
                else:
                    variables = variables + ',' + row[0]
                    values = values + ',' + str(float(row[1]))

    return data