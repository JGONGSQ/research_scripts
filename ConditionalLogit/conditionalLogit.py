#!/usr/bin/python

from collections import OrderedDict
from datetime import datetime

import sys
import subprocess
import pandas as pd
import numpy as np
import pylogit as pl


long_testing_data = pd.read_csv("/Users/daddyspro/Desktop/conditional_logit_test_data.csv")
print(long_testing_data)
# print(long_testing_data.columns)


# general settings
custom_alt_id = "mode_id"

obs_id_column = "choice_situation"

choice_column = "choice"


basic_specification = OrderedDict()
basic_names = OrderedDict()

basic_specification["intercept"] = [1, 2]
basic_names["intercept"] = ['ASC_NSW',
                            'ASC_VIC'
                            ]

basic_specification["distance"] = [1, 2, 3]
basic_names["distance"] = ['distance_NSW',
                           'distance_VIC',
                           'distance_QLD']

basic_specification["male"] = [[1, 2, 3]]
basic_names["male"] = ['male']

basic_specification["agegroup"] = [[1, 2, 3]]
basic_names["agegroup"] = ["agegroup"]

basic_specification["last_choice"] = [[1, 2, 3]]
basic_names["last_choice"] = ['last_choice']

# basic_specification["seat_configuration"] = [2]
# basic_names["seat_configuration"] = ['Airline Seat Configuration, base=No (Swissmetro)']
#
# basic_specification["train_survey"] = [[1, 2]]
# basic_names["train_survey"] = ["Surveyed on a Train, base=No, (Train and Swissmetro)"]
#
# basic_specification["regular_class"] = [1]
# basic_names["regular_class"] = ["First Class == False, (Swissmetro)"]
#
# basic_specification["single_luggage_piece"] = [3]
# basic_names["single_luggage_piece"] = ["Number of Luggage Pieces == 1, (Car)"]
#
# basic_specification["multiple_luggage_pieces"] = [3]
# basic_names["multiple_luggage_pieces"] = ["Number of Luggage Pieces > 1, (Car)"]

# print basic_names
# print basic_specification


destination_mnl = pl.create_choice_model(data=long_testing_data,
                                         alt_id_col=custom_alt_id,
                                         obs_id_col=obs_id_column,
                                         choice_col=choice_column,
                                         specification=basic_specification,
                                         model_type="MNL",
                                         names=basic_names)

destination_mnl.fit_mle(np.zeros(8))
print(destination_mnl.get_statsmodels_summary())


all_situation_ids = np.sort(long_testing_data["choice_situation"].unique())
prediction_ids = all_situation_ids[:2000]
prediction_df = long_testing_data.loc[long_testing_data["choice_situation"].isin(prediction_ids)].copy()

# This is the array of the predicted choice
prediction_array = destination_mnl.predict(prediction_df)

print(prediction_array)


class ConditionalMNL(object):

    def __init__(self):
        pass

    def read_data(self):
        return

    def estimation(self):
        pass

    def forecast(self):
        pass

    def write_results(self):
        pass

    def plot(self):
        pass

    def full(self):
        self.read_data()
        self.estimation()
        self.forecast()
        self.write_results()
        self.plot()
        print("This is a FULL run")
        return


if __name__== '__main__':
    conditional_mnl = ConditionalMNL()
    start_time = datetime.now()

    argv = sys.argv
    try:
        arg = argv[1]
    except Exception:
        arg = 'all'

    if arg == 'read':
        conditional_mnl.read_data()
    elif arg == 'estimation':
        conditional_mnl.estimation()
    elif arg == 'forecast':
        conditional_mnl.forecast()
    elif arg == 'plot':
        conditional_mnl.plot()
    elif arg == "all":
        conditional_mnl.full()

    print(datetime.now() - start_time)