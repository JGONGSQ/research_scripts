#!/usr/bin/python

# imports from local package
from settings import *

# python imports
import csv


class Data(object):

    utility_variables = UTILITY_VARIABLES
    compulsory_fields = COMPULSORY_FIELDS
    state_code = STATE_CODES
    state_list = STATE_LIST
    state_alternatives = STATE_ALTERNATIVES
    alternative_category = ALTERNATIVE_CATEGORY
    output_title = compulsory_fields + alternative_category + utility_variables
    counter = 0

    def __init__(self, source_file, output_file, forecast_file, data=None):
        self.source_file = source_file
        self.output_file = output_file
        self.forecast_file = forecast_file
        self.data = data

    def _get_trips_and_alternatives(self, title_row, row):
        number_of_trips = 0
        alternatives = list()

        number_of_stops = row.__getitem__(title_row.index('NUMSTOP'))

        for i in range(int(number_of_stops)):
            location = row.__getitem__(title_row.index('REGN%s' % str(i+1)))
            state_location = location[0]

            if state_location in self.state_code:
                state_alternative = self.state_alternatives.__getitem__(self.state_code.index(state_location))

                if not alternatives or state_alternative not in alternatives:
                    alternatives.append(state_alternative)
                    number_of_trips += 1
                # elif state_alternative != alternatives[-1]:
                #     number_of_trips += 1

        return number_of_trips, alternatives

    def _bubble_sort_the_alternatives(self, alternatives):
        sort_list = list()

        for alternative in alternatives:
            sort_list.append(alternative)

        for passnumber in range(len(sort_list) - 1, 0, -1):
            for i in range(passnumber):
                if int(sort_list[i]) > int(sort_list[i + 1]):
                    temp = sort_list[i]
                    sort_list[i] = sort_list[i + 1]
                    sort_list[i + 1] = temp
        return sort_list

    def _get_index_of_variables(self, row, variables):
        index = map(row.index, variables)
        # print index
        return index

    def _find_index_in_list(self, list, value):
        index = None
        for i, sub_list in enumerate(list):
            for item in sub_list:
                if item == value:
                    index = i
        return index

    def _get_variable_codes(self, variable):
        code = None
        if variable == 'ORIGIN':
            code = ORIGIN_CODE

        elif variable == 'PARENT':
            code = PARENT_CODE

        elif variable == "GENDER":
            code = GENDER_CODE

        elif variable == 'MARITAL':
            code = MARITAL_CODE

        elif variable == 'EMPLOYMENT':
            code = EMPLOYMENT_CODE

        elif variable == 'HOUSINC':
            code = HOUSINC_CODE

        elif variable == 'LIFECYCLE':
            code = LIFECYCLE_CODE

        elif variable == 'AGEGROUP':
            code = AGEGROUP_CODE

        return code

    def _get_variable_list(self, variable):
        list = None
        if variable == 'ORIGIN':
            list = ORIGIN_LIST

        elif variable == 'PARENT':
            list = PARENT_LIST

        elif variable == "GENDER":
            list = GENDER_LIST

        elif variable == 'MARITAL':
            list = MARITAL_LIST

        elif variable == 'EMPLOYMENT':
            list = EMPLOYMENT_LIST

        elif variable == 'HOUSINC':
            list = HOUSINC_LIST

        elif variable == 'LIFECYCLE':
            list = LIFECYCLE_LIST

        elif variable == 'AGEGROUP':
            list = AGEGROUP_LIST

        return list

    def _get_variable_data(self, variable_code, variable, utility_data):
        # user the variable get variable value in thr row
        variable_value = utility_data.__getitem__(self.utility_variables.index(variable))
        if variable == 'ORIGIN':
            variable_value = variable_value[0]
        # I know the variable code, using the value to find the index value of the value in the code
        index = self._find_index_in_list(variable_code, variable_value)
        # use the index value to get the choose category
        data = self._get_variable_list(variable).__getitem__(index)

        return data

    def _convert_utility_data(self, utility_data):
        converted_data = list()
        # print("This is the utility data", utility_data)

        # For each vaiable in the utility variable list
        for variable in self.utility_variables:
            variable_code = self._get_variable_codes(variable)
            if variable_code:
                variable_data = self._get_variable_data(variable_code, variable, utility_data)
                converted_data.append(variable_data)
            else:
                converted_data.append(utility_data.__getitem__(int(self.utility_variables.index(variable))))
        # print("This is the converted data", converted_data)
        return converted_data

    def _get_useful_data(self, title_row, row, utility_data):
        data = list()

        # get the number of trips in the visit and return the number of the visited
        number_of_trips, alternatives = self._get_trips_and_alternatives(title_row, row)
        tourist_id = row.__getitem__(title_row.index('TOURIST_ID'))

        converted_utility_data = self._convert_utility_data(utility_data)

        # then process each of them into a list
        if number_of_trips > 1:

            # print number_of_trips, alternatives
            sort_list = self._bubble_sort_the_alternatives(alternatives)

            # print(number_of_trips, alternatives, sort_list)
            # for i in range(number_of_trips):
            for alternative in alternatives:
                self.counter += 1
                for choice in sort_list:

                    if alternative == choice:
                        choice_flag = "1"
                    else:
                        choice_flag = "0"

                    row = [tourist_id, self.counter, choice, choice_flag] + converted_utility_data

                    data.append(row)
                    print(row)

            # raise Exception

        return data

    def read(self, filepath):
        self.data = list()

        with open(filepath, 'rU') as csvfile:
            file = csv.reader(csvfile, delimiter=',')
            for row in file:
                self.data.append(row)
            csvfile.close()

        return self.data

    def conditional(self, number_of_data=10000):
        self.read(self.source_file)
        title_row = None
        data = list()

        data.append(self.output_title)

        for i, row in enumerate(self.data):
            # print("### Start of the line ###")
            if i == 0:
                title_row = row
            elif i > number_of_data:
                break
            else:
                utility_data_index = self._get_index_of_variables(title_row, self.utility_variables)
                utility_data = map(row.__getitem__, utility_data_index)
                if ' ' not in utility_data:
                    # print utility_data
                    values = self._get_useful_data(title_row, row, utility_data)

                    for item in values:
                        data.append(item)

        return data

    def write(self, data):

        try:
            with open(self.output_file, 'w') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')

                for row in data:
                    writer.writerow(row)

        except Exception as error:
            raise error

        return True

    def combine(self):
        pass

    def compare(self):
        pass
