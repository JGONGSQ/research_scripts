#!/usr/bin/python
import csv
import math


def get_delta_value(value):
    value = math.log(1/(1-value))
    return value


def get_coef_file(filepath):
    data = list()

    with open(filepath, 'rU') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=',')
        # initial values
        variable_flag = False
        alpha_flag = False
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

            if row[0] == 'D1' or row[0] == 'G1':
                data.append([variables, values])
                # variable_flag = False
                variable_counter = 0
                alpha_flag = True
                variables = ''
                values = ''

            if row[0] == 'sigm':
                data.append([variables, values])
                variable_flag = False

            variable_counter += 1

            if variable_flag:
                value = float(row[1])

                if alpha_flag:
                    if value != 1:
                        value = get_delta_value(value)

                if variable_counter == 1:
                    variables = variables + row[0]
                    values = values + str(value)
                else:
                    variables = variables + ',' + row[0]
                    values = values + ',' + str(value)

    return data