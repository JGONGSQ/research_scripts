#!/usr/bin/python

# Local library imports
from py_files.data import read_ivs_state_combinations, convert_txt_to_csv, \
    write_data_to_csv, convert_list_to_str, get_utility_variables, read_csv_to_data, \
    get_pure_data, count_on_pure_data
from py_files.forecast import get_coef_file, forecast, evaluate
from py_files.plot import *
from mdcev.settings import *

# Python imports
from datetime import datetime
import sys
import subprocess


class ModelRun(object):

    # R script
    r_estimation = 'mdcev/runner_mdcev_nooutside.r'
    r_alpha_forecast = 'mdcev/forecast/run_mdcev_alpha_forecast.r'
    r_gamma_forecast = 'mdcev/forecast/run_mdcev_gamma_forecast.r'

    # CSV data file
    original_source_file = '../Data/ivs/2012/IVS_2012.csv'
    model_data_file = '../Data/ivs/filted_data.csv'
    halton_filepath = INPUT_DIR_PATH + '/Halton.csv'

    # fixed value
    compulsory_fields = COMPULSORY_FIELDS
    alternative_list = STATE_LISTS
    alternative_code = STATE_CODES
    distance_destination_list = DISTANCE_DESTINATION_LIST

    utility_parameters = ['GENDER', 'MARITAL', 'AGEGROUP', 'PARTYPE', 'NUMVISIT',
                          'TRIP_PURPOSE', 'CUSTOMS', 'COUNTRY', 'OTHPURP1']

    # , 'GROUPTYPE' , 'RANDOMSTOP'

    ## OK ##
    # 'MARITAL_SINGLE' 'GENDER_MALE'

    ### NOT CONVERGE ###

    local_variable = ['GENDER_MALE', 'GENDER_FEMALE', 'MARITAL_SINGLE', 'MARITAL_COUPLE', 'AGEGROUP_15_29',
                      'AGEGROUP_30_39', 'AGEGROUP_40_49', 'AGEGROUP_50_59', 'AGEGROUP_60_69', 'AGEGROUP_70_MORE',
                      'PARTYPE_UNACCOMPANIED', 'PARTYPE_ADULT_COUPLE', 'PARTYPE_FAMILY_GROUP',
                      'PARTYPE_FREIEND_RELATIVES', 'PARTYPE_BUSINESS_ASSOCIATES', 'PARTYPE_SCHOOL_TOUR',
                      'TRIP_PURPOSE_HOLIDAY', 'TRIP_PURPOSE_VISITING_FR', 'TRIP_PURPOSE_BUSINESS',
                      'TRIP_PURPOSE_EMPLOYMENT', 'TRIP_PURPOSE_EDUCATION', 'TRIP_PURPOSE_OTHER', 'CUSTOMS_ENTRY_NSW',
                      'CUSTOMS_ENTRY_VIC', 'CUSTOMS_ENTRY_QLD', 'CUSTOMS_ENTRY_SA', 'CUSTOMS_ENTRY_NT',
                      'CUSTOMS_ENTRY_OTHER', 'OTHPURP1']

    # Alternatives
    vic = local_variable
    nt = local_variable
    qld = local_variable
    sa = local_variable
    wa = local_variable
    tas = local_variable
    act = local_variable
    constant = []

    alternatives_utility_variables = [
        # Alternative 2
        vic + constant,
        # Alternative 3
        qld + constant,
        # Alternative 4
        sa + constant,
        # Alternative 5
        wa + constant,
        # Alternative 6
        tas + constant,
        # Alternative 7
        nt + constant,
        # Alternative 8
        act + constant,
    ]

    utility_variables = get_utility_variables(alternatives_utility_variables)
    # case_config_list = [1, 4, 7]
    case_config_list = [4]

    def _create_estimation_output_filename(self, case_config):
        return RESULTS_PATH + '/results' + '_{}'.format(case_config) + '_{}'.format('MDCEV_TEMP') + '.txt'

    def _create_coef_filename(self, case_config):
        return RESULTS_PATH + '/coef' + '_{}'.format(case_config) + '.csv'

    def _create_forecast_filename(self, case_config):
        return RESULTS_PATH + '/results' + '_{}'.format(case_config) + '_{}'.format('MDCEV_forecasting') + '.csv'

    def _get_coef(self, case_config):
        # get the filename by case_config number
        txt_filepath = self._create_estimation_output_filename(case_config)
        csv_filepath = convert_txt_to_csv(txt_filepath)

        coef_data = get_coef_file(csv_filepath)
        coef_file = self._create_coef_filename(case_config)

        flag = write_data_to_csv(filename=coef_file, data=coef_data)
        return flag

    def read_the_data(self):
        flag = read_ivs_state_combinations(
            input_file=self.original_source_file,
            output_file=self.model_data_file,
            compulsory_fields=self.compulsory_fields,
            state_list=self.alternative_list,
            state_codes=self.alternative_code,
            utility_parameters=self.utility_parameters,
            distance_destination_list=self.distance_destination_list,
        )
        return flag

    def estimation(self):
        for case_config in self.case_config_list:

            estimation_output_file = self._create_estimation_output_filename(case_config)
            print('This is the estimation file', estimation_output_file)

            process = subprocess.call(
                ['Rscript --vanilla {r_script} {input_file} '
                 '{number_of_alternatives} {case_config} {utility_parameters} {state_list} {results_file} '
                 '{alternative_2_variables} {alternative_3_variables} {alternative_4_variables} '
                 '{alternative_5_variables} {alternative_6_variables} {alternative_7_variables} {alternative_8_variables}'.format(
                    r_script=self.r_estimation,
                    input_file=self.model_data_file,
                    number_of_alternatives=self.alternative_list.__len__(),
                    case_config=case_config,
                    utility_parameters=convert_list_to_str(self.utility_variables),
                    state_list=convert_list_to_str(self.alternative_list),
                    results_file=estimation_output_file,
                    alternative_2_variables=convert_list_to_str(self.alternatives_utility_variables[0]),
                    alternative_3_variables=convert_list_to_str(self.alternatives_utility_variables[1]),
                    alternative_4_variables=convert_list_to_str(self.alternatives_utility_variables[2]),
                    alternative_5_variables=convert_list_to_str(self.alternatives_utility_variables[3]),
                    alternative_6_variables=convert_list_to_str(self.alternatives_utility_variables[4]),
                    alternative_7_variables=convert_list_to_str(self.alternatives_utility_variables[5]),
                    alternative_8_variables=convert_list_to_str(self.alternatives_utility_variables[6]),)
                ]
                , shell=True)
        return

    def forecast(self):
        for case_config in self.case_config_list:
            self._get_coef(case_config)
            r_file = self.r_alpha_forecast
            if case_config == 4:
                r_file = self.r_gamma_forecast

            forecast(r_file=r_file, data_filepath=self.model_data_file,
                     case_config=case_config, results_file=self._create_forecast_filename(case_config),
                     halton_filepath=self.halton_filepath, coef_file=self._create_coef_filename(case_config))

            evaluate(data_file=self.model_data_file, result_file=self._create_forecast_filename(case_config), alternative_list=STATE_LISTS)

        return

    def plot(self):
        for case_config in self.case_config_list:
            # Read the result from csv file and get the index number of the data
            data = read_csv_to_data(self.model_data_file)
            data_alternative_index = map(data[0].index, STATE_LISTS)

            result = read_csv_to_data(self._create_forecast_filename(case_config))
            result_alternative_index = map(result[0].index, STATE_LISTS)
            # print data_alternative_index, result_alternative_index

            # Get the pure data
            pure_data = get_pure_data(data, data_alternative_index)
            pure_result = get_pure_data(result, result_alternative_index)

            # Initial some list to storing values
            number_of_alternatives = data_alternative_index.__len__()  # == 6 in this model

            data_duration_counts, data_alternative_counts, data_number_of_chosen_alternative_counts = count_on_pure_data(
                pure_data, number_of_alternatives)
            result_duration_counts, result_alternative_counts, result_number_of_chosen_alternative_counts = count_on_pure_data(
                pure_result, number_of_alternatives)

            print data_duration_counts, result_duration_counts
            print data_alternative_counts, result_alternative_counts
            print data_number_of_chosen_alternative_counts, result_number_of_chosen_alternative_counts

            # Plotting part
            fig = plt.figure(case_config)

            fig = plot_bar_graph_within(STATE_LISTS, data_duration_counts, result_duration_counts,
                                        'Duration counts in days', fig, 221)
            fig = plot_bar_graph_within(STATE_LISTS, data_alternative_counts, result_alternative_counts,
                                        'Alternative counts as correct ratio', fig, 222)
            fig = plot_bar_graph_within([1, 2, 3, 4, 5, 6], data_number_of_chosen_alternative_counts,
                                        result_number_of_chosen_alternative_counts, "Number of chosen alternative hit",
                                        fig, 223)

        # This will show all the figures generated by the plot function.
        plt.show()
        return

    def full(self):
        # self.read_the_data()
        self.estimation()
        # self.forecast()
        # self.plot()
        return


if __name__ == '__main__':
    model_run = ModelRun()
    start_time = datetime.now()

    argv = sys.argv
    try:
        arg = argv[1]
    except Exception:
        arg = 'all'

    if arg == 'read':
        model_run.read_the_data()

    elif arg == 'estimation':
        model_run.estimation()

    elif arg == 'forecast':
        model_run.forecast()

    elif arg == 'plot':
        model_run.plot()

    elif arg == 'all':
        model_run.full()

    print(datetime.now() - start_time)



