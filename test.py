#!/usr/bin/python

# Import the packagess
from py_files.data import get_code_address, update_regn_dict, write_data_to_csv, get_regn_dict, read_csv_to_data
from py_files.settings import *
from py_files.forecast import evaluate
import numpy as np
import matplotlib.pyplot as plt


data_filepath = INPUT_DIR_PATH + '/NVS2007_trimed_v3.csv'
results_file = RESULTS_PATH + '/results' + '_{}'.format(1) + '_{}'.format('MDCEV_forecasting') + '.csv'

# evaluate(data_file=data_filepath, result_file=results_file, alternative_list=STATE_LISTS)

x = np.linspace(0, 1, 500)
print x
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)

fig, ax = plt.subplots()

# ax.fill(x, y, zorder=10)
# ax.grid(True, zorder=5)
# plt.show()
#
# data = read_csv_to_data(results_file)
# for row in data:
#     print(row)

