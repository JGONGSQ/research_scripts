#!/usr/bin/python
import subprocess

from py_files.forecast import *
from py_files.settings import *
from py_files.data import *
from py_files.plot import *

r_file = 'r_files/forecast/run_mdcev_alpha_forecast.r'
txt_filepath = '/Users/daddyspro/Desktop/useful_results/mutiple_utility_model/results_1_MDCEV_2.txt'
halton_filepath = INPUT_DIR_PATH + '/Halton.csv'
data_filepath = INPUT_DIR_PATH + '/NVS2007_trimed_v3.csv'
results_file = RESULTS_PATH + '/results' + '_{}'.format(1) + '_{}'.format('MDCEV_forecasting') + '.csv'
coef_file = INPUT_DIR_PATH + '/coef.csv'

csv_filepath = convert_txt_to_csv(txt_filepath)
print csv_filepath

coef_data = get_coef_file(csv_filepath)
write_data_to_csv(filename=coef_file, data=coef_data)

case_config = 1

forecast(r_file=r_file, data_filepath=data_filepath,
         case_config=case_config, results_file=results_file,
         halton_filepath=halton_filepath, coef_file=coef_file)


# evaluate the result
evaluate(data_file=data_filepath, result_file=results_file, alternative_list=STATE_LISTS)


# Read the result from csv file and get the index number of the data
data = read_csv_to_data(data_filepath)
data_alternative_index = map(data[0].index, STATE_LISTS)

result = read_csv_to_data(results_file)
result_alternative_index = map(result[0].index, STATE_LISTS)
print data_alternative_index, result_alternative_index

# Get the pure data
pure_data = get_pure_data(data, data_alternative_index)
pure_result = get_pure_data(result, result_alternative_index)

# Initial some list to storing values
number_of_alternatives = data_alternative_index.__len__() # == 6 in this model

data_duration_counts, data_alternative_counts, data_number_of_chosen_alternative_counts = count_on_pure_data(pure_data,number_of_alternatives)
result_duration_counts, result_alternative_counts, result_number_of_chosen_alternative_counts = count_on_pure_data(pure_result, number_of_alternatives)

print data_duration_counts, result_duration_counts
print data_alternative_counts, result_alternative_counts
print data_number_of_chosen_alternative_counts, result_number_of_chosen_alternative_counts

# Plotting part
fig = plt.figure(4)

fig = plot_bar_graph_within(STATE_LISTS, data_duration_counts, result_duration_counts, 'Duration counts in days', fig, 221)
fig = plot_bar_graph_within(STATE_LISTS, data_alternative_counts, result_alternative_counts, 'Alternative counts as hit ratio', fig, 222)
fig = plot_bar_graph_within([1,2,3,4,5,6], data_number_of_chosen_alternative_counts, result_number_of_chosen_alternative_counts, "Number of chosen alternative hit", fig, 223)

plt.show()


# if __name__ == '__main__':
#     print 123123123