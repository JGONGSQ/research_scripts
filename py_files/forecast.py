#!/usr/bin/python
import csv
import math
import numpy as np


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


def compare_data_and_result(data, result):
    """
        Comparing the forecasted results and original data
    :param data: original data list
    :param result: forecasted results list
    :return: hit ratio and r_square value of each row
    """
    data = map(float, data)
    result = map(float, result)
    data_avg = sum(data) / len(data)
    number_of_choice = float(np.count_nonzero(data))
    number_of_hit = float(0)

    tot = float(0)
    resisudal = float(0)
    for i, number in enumerate(data):
        if number != 0 and result[i] != 0:
            number_of_hit += 1
            resisudal += (result[i] - data[i]) ** 2

        tot += (data[i] - data_avg) ** 2

    hit = round(number_of_hit / number_of_choice, 3)
    r_square = 1 - round(resisudal / tot, 3)
    print hit, r_square

    return hit, r_square


def evaluate(data_file, result_file, alternative_list=None):
    """
    :param data_file: original data file
    :param result_file: results of the forecasting operation
    :param alternative_list: list of alternatives
    :return:
    """
    hit_ratio = list()
    r_square = list()
    with open(data_file, 'rU') as data_csv, open(result_file, 'r+') as result_file:

        data_reader = csv.reader(data_csv, delimiter=',')
        result_reader = csv.reader(result_file, delimiter=',')

        for i, data_row in enumerate(data_reader):

            if i == 0:
                data_row_index = map(data_row.index, alternative_list)
                result_row_index = map(result_reader.next().index, alternative_list)
                print data_row_index, result_row_index
            else:
                result_row = result_reader.next()
                data = map(data_row.__getitem__, data_row_index)
                result = map(result_row.__getitem__, result_row_index)
                print data, result
                hit, r = compare_data_and_result(data, result)
                hit_ratio.append(hit)
                r_square.append(r)
                # raise Exception
    average_hit = sum(hit_ratio)/len(hit_ratio)
    average_r = sum(r_square)/len(r_square)
    print("This is the average hit", average_hit)
    print("This is the average r square", average_r)
    return


def forecast(r_file, data_filepath, case_config, results_file, halton_filepath, coef_file):
    """
    :param r_file: It is the R file going to use for the forecasting
    :param data_filepath: It is the data file of the original estimation. normally would be a csv file
    :param case_config: it the case_configureation of the forecasting, nomally would 1, 4, 7
    :param results_file: forecasting results file, which is the output file
    :param halton_filepath: the file generate the randomsy in the forecasting
    :param coef_file: the file of the coef file store in the csv, normally would be convert from a txt file.
    :return:
    """
    process = subprocess.call(
        ['Rscript --vanilla {r_file} {data_file} '
         '{number_of_alternatives} {case_config} {state_list} {results_file} '
         '{halton_file} {coef_file}'.format(
            r_file=r_file,
            data_file=data_filepath,  # 1
            number_of_alternatives=STATE_LISTS.__len__(),
            case_config=case_config,  # 3
            state_list=convert_list_to_str(STATE_LISTS),
            results_file=results_file,  # 5
            halton_file=halton_filepath,
            coef_file=coef_file  # 7
        )
        ]
        , shell=True)

    return