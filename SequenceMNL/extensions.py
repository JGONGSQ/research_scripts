#!/usr/bin/python
# imports from local package
import csv
import sys
# sys.path.append('../')

from settings import *
# from py_files.data import *
# python imports

from geopy.distance import vincenty


class Data(object):

    all_variables = ALL_VARIABLES
    utility_variables = UTILITY_VARIABLES
    state_codes = STATE_CODES
    state_list = STATE_LIST
    compulsory_fields = COMPULSORY_FIELDS
    output_title = compulsory_fields + FROM_TO + utility_variables + DISTANCE
    counter = 0

    # initial
    def __init__(self, source_file, output_file, forecast_file, data=None):
        self.source_file = source_file
        self.output_file = output_file
        self.forecast_file = forecast_file
        self.data = data

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

        elif variable == 'PARENT':
            code = PARENT_CODE

        # elif variable == 'YOUNGEST':
        #     code = YOUNGEST_CODE

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

        elif variable == 'PARENT':
            list = PARENT_LIST

        elif variable == 'YOUNGEST':
            list = YOUNGEST_LIST

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

    def _get_variable_data(self, variable_code, variable, utility_data):
        # user the variable get variable value in thr row
        variable_value = utility_data.__getitem__(self.utility_variables.index(variable))
        if variable == 'HOMEREGN':
            variable_value = variable_value[0]
        # I know the variable  code, using the value to find the index value of the value in the code
        index = self._find_index_in_list(variable_code, variable_value)
        # use the index value to get the choose category
        data = self._get_variable_list(variable).__getitem__(index)

        return data

    def _convert_utility_data(self, utility_data):
        converted_data = list()
        print("This is the utility data", utility_data)

        # For each vaiable in the utility variable list
        for variable in self.utility_variables:
            variable_code = self._get_variable_codes(variable)
            if variable_code:
                variable_data = self._get_variable_data(variable_code, variable, utility_data)
                converted_data.append(variable_data)
            else:
                converted_data.append(utility_data.__getitem__(int(self.utility_variables.index(variable))))
        print("This is the converted data", converted_data)
        return converted_data

    def _get_index_of_variables(self, row, variables):
        index = map(row.index, variables)
        # print index
        return index

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
        print(from_origin, to_destination)

        distance = vincenty(from_origin, to_destination).km

        # round the distance to the closest km
        return int(distance)

    def _get_vistied_sequence_in_state(self, title_row, row, origin_data, regn_dict):
        sequence = list()
        distances = list()
        last_visited = None

        number_of_stops = row.__getitem__(title_row.index('NUMSTOP'))
        # print("This is the number of stops", number_of_stops)

        for i in range(int(number_of_stops)):
            # get the location of the travel regn
            visiting_location = row.__getitem__(title_row.index('REGN%s' % str(i + 1)))
            print("This is the location code", visiting_location, origin_data)
            state_location = visiting_location[0]
            # print(state_location)

            if i == 0:
                last_visited = origin_data
            else:
                last_visited = row.__getitem__(title_row.index('REGN%s' % str(i)))

            distance = self.cal_distance_v2(regn_dict[last_visited], regn_dict[visiting_location])

            if state_location in self.state_codes:
                state_name = self.state_list.__getitem__(self.state_codes.index(state_location))
                # print state_name
                if not sequence or sequence[-1] != state_name:
                    # sequence.append(state_name)
                    sequence.append(state_name)
                    distances.append(distance)

        return sequence, distances

    def _get_useful_data(self, title_row, row, utility_data):
        # get the category variables
        data = list()

        # get the region dict
        regn_dict = self._get_regn_dict(REGN_CODE_DICT_PATH_V2)

        converted_utility_data = self._convert_utility_data(utility_data)
        origin_data = utility_data.__getitem__(self.utility_variables.index('HOMEREGN'))
        # line = map(row.__getitem__, index)

        state_sequence, distances = self._get_vistied_sequence_in_state(title_row, row, origin_data, regn_dict)
        print("State Sequence", state_sequence)
        compulsory_data = map(row.__getitem__, self._get_index_of_variables(title_row, self.compulsory_fields))
        # print("This is the compulsory_data", compulsory_data)

        # convert sequence into needy form
        print("This is the origin data", origin_data[0])
        from_to_data = ["0", origin_data]
        for i, item in enumerate(state_sequence):
            self.counter += 1
            compulsory_data[0] = self.counter
            # # distance need to be calcualted
            distance = [distances[i]]
            from_to_data[0] = item
            if i != 0:
                from_to_data[1] = state_sequence[i-1]

            local_list = compulsory_data + from_to_data + converted_utility_data + distance
            data.append(local_list)
            break

        # sperated them as different list if have multiple destinations

        # return the list object
        return data

    # read
    def read(self, filepath):
        self.data = list()
        with open(filepath, 'rU') as csvfile:
            file = csv.reader(csvfile, delimiter=',')
            for row in file:
                self.data.append(row)
            csvfile.close()
        return self.data

    # Get the sequence of the data
    def sequence(self, number_of_data=50000):
        self.read(self.source_file)
        title_row = None
        data = list()

        data.append(self.output_title)

        # self.data are from the self.read method
        for i, row in enumerate(self.data):
            print("############ Start of each line")
            if i == 0:
                # print(i, row)
                title_row = row
            elif i > number_of_data:
                break
            else:
                # check the utility data
                utility_data_index = self._get_index_of_variables(title_row, self.utility_variables)
                utility_data = map(row.__getitem__, utility_data_index)
                print("@##@@#@#", utility_data)
                # print(utility_data)

                # if no missing data in the range, do the processing otherwise pass
                if ' ' not in utility_data:

                    # read the row and write it to the line
                    values = self._get_useful_data(title_row, row, utility_data)
                    # insert the line genereated by the values
                    for item in values:
                        data.append(item)
                    # print("Data processing", data)

                    # raise Exception

        # for item in data:
        #     print item

        return data

    # write
    def write(self, data):
        """
            Write the results list to generate a new data file
        """
        # open the file need to be write
        try:
            with open(self.output_file, 'w') as csvfile:
                # initial the writer
                writer = csv.writer(csvfile, delimiter=',')

                # write each row
                for row in data:
                    writer.writerow(row)

        except Exception as error:
            print error
            return False

        return True

    # combine
    def combine(self):
        pass

    # compare
    def compare(self):
        counter = 0
        hit_ratio = float()
        origin_data = self.read(self.output_file)
        forecast_data = self.read(self.forecast_file)
        destiantion_index = 3
        total_number_of_data = origin_data.__len__()
        for i in range(total_number_of_data):
            if i == 0:
                pass
            else:
                if origin_data[i][destiantion_index] == forecast_data[i][1]:
                    counter += 1

        hit_ratio = float(counter) / total_number_of_data
        print(counter, hit_ratio)
        return


class R(object):
    pass



