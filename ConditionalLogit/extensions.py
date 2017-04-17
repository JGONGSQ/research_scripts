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

    def _get_useful_data(self, title_row, row, utility_data):
        data = list()

        # get the number of trips in the visit and return the number of the visited
        number_of_trips, alternatives = self._get_trips_and_alternatives(title_row, row)

        # then process each of them into a list
        if number_of_trips > 1:

            # print number_of_trips, alternatives
            sort_list = self._bubble_sort_the_alternatives(alternatives)

            print(number_of_trips, alternatives, sort_list)
            # for i in range(number_of_trips):
            for alternative in alternatives:
                self.counter += 1
                for choice in sort_list:

                    if alternative == choice:
                        choice_flag = "1"
                    else:
                        choice_flag = "0"

                    row = [self.counter, choice, choice_flag] + utility_data

                    print(row)

            raise Exception

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
