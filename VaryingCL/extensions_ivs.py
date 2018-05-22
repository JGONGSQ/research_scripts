#!/usr/bin/python

# imports from local package
from settings_ivs import *

# python imports
import csv
from geopy.distance import vincenty


class Data(object):

    utility_variables = UTILITY_VARIABLES
    compulsory_fields = COMPULSORY_FIELDS
    state_code = STATE_CODES
    state_list = STATE_LIST
    state_alternatives = STATE_ALTERNATIVES
    alternative_category = ALTERNATIVE_CATEGORY
    output_title = compulsory_fields + alternative_category + VISITED_FROM + utility_variables + ['Distance']
    counter = 0
    user_id = 0

    def __init__(self, source_file, output_file, forecast_file, data=None):
        self.source_file = source_file
        self.output_file = output_file
        self.forecast_file = forecast_file
        self.data = data

    def cal_distance_v2(self, point_1, point_2):
        """
            Calculate the distance between points
        :param origin_name: such as 'TAS', 'NSW' or 'TAS'
        :param destination_name: same as origin code
        :return: distance between two point in km
        """

        # make the points
        from_origin = (point_1["latitude"], point_1["longitude"])
        to_destination = (point_2["latitude"], point_2["longitude"])
        # print(from_origin, to_destination)

        distance = vincenty(from_origin, to_destination).km

        # round the distance to the closest km
        return int(distance)

    def _get_trips_and_alternatives(self, title_row, row):
        number_of_trips = 0
        alternatives = list()
        locations = list()

        number_of_stops = row.__getitem__(title_row.index('NUMSTOP'))

        for i in range(int(number_of_stops)):
            location = row.__getitem__(title_row.index('REGN%s' % str(i+1)))
            state_location = location[0]

            if state_location in self.state_code:
                state_alternative = self.state_alternatives.__getitem__(self.state_code.index(state_location))

                if not alternatives or state_alternative not in alternatives:
                    alternatives.append(state_alternative)
                    locations.append(location)
                    number_of_trips += 1
                # elif state_alternative != alternatives[-1]:
                #     number_of_trips += 1

        return number_of_trips, alternatives, locations

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
        if variable == 'HOMEREGN':
            code = ORIGIN_CODE

        elif variable == 'ORIGIN':
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
        if variable == 'HOMEREGN':
            list = ORIGIN_LIST

        elif variable == 'ORIGIN':
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

    def _get_variable_category(self, variable):
        category = None
        if variable == 'HOMEREGN':
            category = ORIGIN_CATEGORY

        elif variable == 'ORIGIN':
            category = ORIGIN_CATEGORY

        elif variable == 'PARENT':
            category = PARENT_CATEGORY

        elif variable == "GENDER":
            category = GENDER_CATEGORY

        elif variable == 'MARITAL':
            category = MARITAL_CATEGORY

        elif variable == 'EMPLOYMENT':
            category = EMPLOYMENT_CATEGORY

        elif variable == 'HOUSINC':
            category = HOUSINC_CATEGORY

        elif variable == 'LIFECYCLE':
            category = LIFECYCLE_CATEGORY

        elif variable == 'AGEGROUP':
            category = AGEGROUP_CATEGORY

        return category

    def _get_utility_parameters_list(self, utility_parameters):
        utility_parameters_list = list()

        for variable in utility_parameters:

            variable_list = self._get_variable_list(variable)
            if variable_list:
                utility_parameters_list += variable_list
            else:
                utility_parameters_list.append(variable)

        return utility_parameters_list

    def _get_variable_data(self, variable_code, variable, utility_data):
        # user the variable get variable value in thr row
        variable_value = utility_data.__getitem__(self.utility_variables.index(variable))
        if variable == 'HOMEREGN':
            variable_value = variable_value[0]
        # I know the variable code, using the value to find the index value of the value in the code
        index = self._find_index_in_list(variable_code, variable_value)
        # use the index value to get the choose category
        data = self._get_variable_category(variable).__getitem__(index)

        return data

    def _get_utility_variable_data(self, title_row, row, variable, variable_code, variable_list):
        # variable_data = [0] * variable_code.__len__()
        variable_data = None
        value = row.__getitem__(title_row.index(variable))

        if variable == 'HOMEREGN':
            value = value[0]

        print("### This is the value in the line:", value)
        if value:
            variable_data = [variable_list[self._find_index_in_list(list=variable_code, value=value)]]

        return variable_data

    def _convert_utility_data(self, title_row, row, utility_data):
        converted_data = list()
        # print("This is the utility data", utility_data)

        # For each vaiable in the utility variable list
        for variable in self.utility_variables:
            variable_code = self._get_variable_codes(variable)
            variable_list = self._get_variable_list(variable)
            if variable_code:
                # variable_data = self._get_variable_data(variable_code, variable, utility_data)
                variable_data = self._get_utility_variable_data(
                    title_row=title_row,
                    row=row,
                    variable=variable,
                    variable_code=variable_code,
                    variable_list=variable_list
                )

                converted_data += variable_data
            else:
                converted_data.append(utility_data.__getitem__(int(self.utility_variables.index(variable))))
        # print("This is the converted data", converted_data)
        return converted_data

    def _get_regn_dict(self, filepath):
        regn_dict = {}

        with open(filepath, 'rU') as input_csv:
            file_reader = csv.reader(input_csv, delimiter=',')
            for i, row in enumerate(file_reader):
                key = row[0]
                latitude = row[2]
                longitude = row[3]
                regn_dict[key] = {
                    "latitude": latitude,
                    "longitude": longitude
                }

        return regn_dict

    def _get_useful_data(self, title_row, row, utility_data, regn_dict):
        data = list()
        choiceid = 0

        origin_data = utility_data.__getitem__(self.utility_variables.index('HOMEREGN'))

        # get the number of trips in the visit and return the number of the visited
        number_of_trips, alternatives, locations = self._get_trips_and_alternatives(title_row, row)
        tourist_id = row.__getitem__(title_row.index('TOURIST_ID'))
        # print(utility_data)
        converted_utility_data = self._convert_utility_data(title_row, row, utility_data)
        print("Converted Data", converted_utility_data)
        # raise Exception

        # then process each of them into a list
        if number_of_trips > 1:
            self.user_id += 1
            # print number_of_trips, alternatives
            sort_alternatives = self._bubble_sort_the_alternatives(alternatives)
            sort_locations = self._bubble_sort_the_alternatives(locations)
            print("######## This is the locations", tourist_id, locations, sort_locations, origin_data)
            # print(number_of_trips, alternatives, sort_list)
            # for i in range(number_of_trips):
            for i, alternative in enumerate(alternatives):
                self.counter += 1
                choiceid += 1

                if i == 0:
                    last_visited = origin_data
                else:
                    last_visited = locations[i - 1]

                k = 0
                for j, choice in enumerate(sort_alternatives):

                    if alternative == choice:
                        choice_flag = "yes"
                    else:
                        choice_flag = "no"

                    if i == 0 or last_visited != sort_locations[j]:
                        k += 1
                        distance = self.cal_distance_v2(regn_dict[last_visited], regn_dict[sort_locations[j]])
                        print("### This is last visited State code", last_visited)
                        last_visited_state = ORIGIN_STATE_LIST[ORIGIN_STATE_CODES.index(last_visited[0])]

                        if distance == 0:
                            distance = 50

                        row = [self.user_id, choiceid, self.counter, k, STATE_LIST[STATE_ALTERNATIVES.index(choice)], choice_flag] + [last_visited_state] + converted_utility_data + [distance]

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

    def vcl(self, number_of_data=50000):
        self.read(self.source_file)
        title_row = None
        data = list()
        regn_dict = self._get_regn_dict(REGN_CODE_DICT_PATH_V2)

        # data.append(self._get_utility_parameters_list(self.output_title))
        data.append(self.output_title)

        for i, row in enumerate(self.data):
            # print("### Start of the line ###")
            if i == 0:
                title_row = row
            elif i > number_of_data:
                print("### Reach the number of data required")
                break
            else:
                utility_data_index = self._get_index_of_variables(title_row, self.utility_variables)
                utility_data = map(row.__getitem__, utility_data_index)
                if ' ' not in utility_data:
                    # print utility_data
                    values = self._get_useful_data(title_row, row, utility_data, regn_dict)

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
