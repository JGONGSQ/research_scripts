#!/usr/bin/python
from settings import *
from extensions import Data

from collections import OrderedDict
from datetime import datetime


import sys
import subprocess
import pandas as pd
import numpy as np
import pylogit as pl

############### Start ##################

# utility function settings
basic_specification = OrderedDict()
basic_names = OrderedDict()

basic_specification["intercept"] = [1, 2]
basic_names["intercept"] = [
    'ASC_NSW',
    'ASC_VIC'
]

basic_specification["HOMESLA"] = [1, 2, 3]
basic_names["HOMESLA"] = [
    'HOMESLA_NSW',
    'HOMESLA_VIC',
    'HOMESLA_QLD'
]

basic_specification["GENDER"] = [[1, 2, 3]]
basic_names["GENDER"] = ['GENDER']

basic_specification["AGEGROUP"] = [[1, 2, 3]]
basic_names["AGEGROUP"] = ["AGEGROUP"]

basic_specification["ORIGIN"] = [[1, 2, 3]]
basic_names["ORIGIN"] = ["ORIGIN"]

basic_specification["EMPLOYMENT"] = [[1, 2, 3]]
basic_names["EMPLOYMENT"] = ["EMPLOYMENT"]

total_num_parameters = 0
for item in basic_names:
    total_num_parameters += basic_names[item].__len__()


class ConditionalMNL(object):

    model_mnl = None

    # csv data files
    original_source_file = SOURCE_INPUT_FILE
    output_file = OUTPUT_FILE
    forecast_file = FORECAST_FILE

    # pylogit settings
    custom_alt_id = "alternative_id"
    obs_id_column = "choice_situation"
    choice_column = "choice"

    def __init__(self):
        self.data = Data(source_file=self.original_source_file,
                         output_file=self.output_file,
                         forecast_file=self.forecast_file)

    def read_data(self):
        conditional_data = self.data.conditional()
        self.data.write(conditional_data)
        return

    def estimation(self):
        long_testing_data = pd.read_csv(self.output_file)

        self.model_mnl = pl.create_choice_model(
            data=long_testing_data,
            alt_id_col=self.custom_alt_id,
            obs_id_col=self.obs_id_column,
            choice_col=self.choice_column,
            specification=basic_specification,
            model_type="MNL",
            names=basic_names
        )

        self.model_mnl.fit_mle(np.zeros(total_num_parameters))
        print(self.model_mnl.get_statsmodels_summary())

        # all_situation_ids = np.sort(long_testing_data["choice_situation"].unique())
        # prediction_ids = all_situation_ids[:2000]

        return

    def forecast(self):
        # read the data
        long_testing_data = pd.read_csv(self.output_file)
        # some local settings
        all_situation_ids = np.sort(long_testing_data["choice_situation"].unique())
        prediction_ids = all_situation_ids[:2000]
        prediction_df = long_testing_data.loc[long_testing_data["choice_situation"].isin(prediction_ids)].copy()
        # predict call
        prediction_array = self.model_mnl.predict(prediction_df)

        print(prediction_array)
        return

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