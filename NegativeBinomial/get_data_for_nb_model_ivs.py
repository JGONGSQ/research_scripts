#!/usr/bin/python

from settings import *

# imports
import csv
import sys
from datetime import datetime


class ReadData(object):

    def write_data_to_csv(self, filename, data):
        # open the file need to be write
        with open(filename, 'w') as csvfile:
            # initial the writer
            writer = csv.writer(csvfile, delimiter=',')

            # write each row
            for row in data:
                writer.writerow(row)

        return True

    def get_the_variable_code(self, variable):

        variable_codes = None

        if variable == 'ORIGIN':
            variable_codes = ORIGIN_CODE

        elif variable == 'PARENT':
            variable_codes = PARENT_CODE

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

        elif variable == 'CH15TO24':
            variable_codes = CH15TO24_CODE

        elif variable == 'PARTYPE':
            variable_codes = PARTYPE_CODE

        elif variable == 'GROUPTYPE':
            variable_codes = GROUPTYPE_CODE

        elif variable == 'TRIP_PURPOSE':
            variable_codes = TRIP_PURPOSE_CODE

        elif variable == 'CUSTOMS':
            variable_codes = CUSTOMS_CODE

        return variable_codes

    def get_the_variable_list(self, variable):
        variable_list = None

        if variable == 'ORIGIN':
            variable_list = ORIGIN_LIST

        elif variable == 'PARENT':
            variable_list = PARENT_LIST

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

        elif variable == 'CH15TO24':
            variable_list = CH15TO24_LIST

        elif variable == 'PARTYPE':
            variable_list = PARTYPE_LIST

        elif variable == 'GROUPTYPE':
            variable_list = GROUPTYPE_LIST

        elif variable == 'TRIP_PURPOSE':
            variable_list = TRIP_PURPOSE_LIST

        elif variable == 'CUSTOMS':
            variable_list = CUSTOMS_LIST

        return variable_list

    def get_the_utility_variable_data(self, utility_data, utility_parameters, variable, variable_codes, variable_list):
        data_value = utility_data[utility_parameters.index(variable)]
        variable_data = None

        for i, item in enumerate(variable_codes):
            # print(data_value, item)
            if data_value in item:
                variable_data = variable_list[i]
                # print(variable_data)

        return variable_data

    def converte_utility_data(self, utility_data, utility_parameters):

        value_list = list()

        # For each parameters
        for variable in utility_parameters:
            # print(variable)

            # get the parameter value
            variable_codes = self.get_the_variable_code(variable)
            variable_list = self.get_the_variable_list(variable)

            # converted into text if needed
            if variable_codes:
                variable_data = self.get_the_utility_variable_data(
                    utility_data=utility_data,
                    utility_parameters=utility_parameters,
                    variable=variable,
                    variable_codes=variable_codes,
                    variable_list=variable_list
                )

                value_list.append(variable_data)
            else:
                value_list.append(utility_data.__getitem__(int(utility_parameters.index(variable))))
            # else store the value

        return value_list

    def get_line(self, input_file, output_file, utility_parameters, number_of_data=50000):
        data = list()
        input_field_list = None
        # index_number = 1
        compulsory_fields = ['id', 'uno', 'sero', 'NUMSTOP', 'AUSNITES']
        output_fields_list = compulsory_fields + utility_parameters

        data.append(output_fields_list)

        with open(input_file, 'rU') as input_csv:
            file_reader = csv.reader(input_csv, delimiter=',')

            for i, row in enumerate(file_reader):
                if i == 0:
                    input_field_list = row
                elif i > number_of_data:
                    break
                else:
                    # print(row)
                    utility_data = map(row.__getitem__, map(input_field_list.index, utility_parameters))
                    print(utility_data)

                    if ' ' not in utility_data:
                        # output_row = [0] * output_fields_list.__len__()
                        compulsory_data = map(row.__getitem__, map(input_field_list.index, compulsory_fields))
                        converted_utility_data = self.converte_utility_data(utility_data, utility_parameters)
                        print("####", converted_utility_data)


                        data_set = compulsory_data + converted_utility_data

                        data.append(data_set)
                        # raise Exception

        is_successful = self.write_data_to_csv(filename=output_file, data=data)

        return is_successful


if __name__ == '__main__':
    print("### Starts processing the data for NB model ###")

    input_file = '../../Data/ivs/2012/IVS_2012.csv'
    output_file = '../../Data/ivs/2012/NB_Model_IVS_2012.csv'
    utility_parameters = ['GENDER', 'MARITAL', 'AGEGROUP', 'PARTYPE', 'GROUPTYPE', 'NUMSTOP', 'NUMVISIT',
                          'TRIP_PURPOSE', 'CUSTOMS', 'COUNTRY', 'OTHPURP1']

    read_data = ReadData()
    read_data.get_line(input_file, output_file, utility_parameters)




