#!/usr/bin/python
from basics import *
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


total_num_parameters = 0
for item in basic_names:
    total_num_parameters += basic_names[item].__len__()


class ConditionalMNL(object):

    # csv data files
    original_source_file = SOURCE_INPUT_FILE
    output_file = OUTPUT_FILE
    forecast_file = FORECAST_FILE

    # pylogit settings
    custom_alt_id = "mode_id"
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

    def estimation_mnl(self):
        long_testing_data = pd.read_csv(self.output_file)

        print("################################################ MNL Model ######################################")

        model_mnl = pl.create_choice_model(
            data=long_testing_data,
            alt_id_col=self.custom_alt_id,
            obs_id_col=self.obs_id_column,
            choice_col=self.choice_column,
            specification=basic_specification,
            model_type="MNL",
            names=basic_names
        )

        model_mnl.fit_mle(np.zeros(total_num_parameters))
        results = model_mnl.get_statsmodels_summary()

        print("########################", results)

        # all_situation_ids = np.sort(long_testing_data["choice_situation"].unique())
        # prediction_ids = all_situation_ids[:2000]

        return model_mnl

    def estimation_asym(self, model_mnl):
        # read the data
        long_testing_data = pd.read_csv(self.output_file)

        # Set up the asym specifaction and names dictionary
        asym_specification = OrderedDict()
        asym_names = OrderedDict()

        for col in basic_specification:
            if col != "intercept":
                asym_specification[col] = basic_specification[col]
                asym_names[col] = basic_names[col]

        asym_intercept_names = basic_names["intercept"]

        # the "index" of the alternative whose constant has been constrained
        asym_intercept_ref_pos = 4

        # "shape_TAS" is not presented
        asym_shape_names = ["shape_NSW", "shape_VIC", "shape_QLD", "shape_SA"]
        number_of_initial_values = len(asym_shape_names)

        # the "index" of the alternative whose shape parameter is constrained
        asym_ref = 4

        print("################################################## Asymmetry Model #########################################")

        model_asym = pl.create_choice_model(
            data=long_testing_data,
            alt_id_col=self.custom_alt_id,
            obs_id_col=self.obs_id_column,
            choice_col=self.choice_column,
            specification=asym_specification,
            model_type="Asym",
            names=asym_names,
            shape_names=asym_shape_names,
            intercept_names=asym_intercept_names,
            shape_ref_pos=asym_ref,
            intercept_ref_pos=asym_intercept_ref_pos
        )

        model_asym.fit_mle(
            None,
            init_shapes=np.zeros(number_of_initial_values),
            init_intercepts=model_mnl.params.values[:number_of_initial_values],
            init_coefs=model_mnl.params.values[number_of_initial_values:] / np.log(number_of_initial_values+1),
            method="bfgs"
        )

        model_asym.get_statsmodels_summary()

        return model_asym

    def forecast(self, model):
        # read the data
        long_testing_data = pd.read_csv(self.output_file)
        # some local settings
        all_situation_ids = np.sort(long_testing_data["choice_situation"].unique())
        prediction_ids = all_situation_ids[:2000]
        prediction_df = long_testing_data.loc[long_testing_data["choice_situation"].isin(prediction_ids)].copy()
        # predict call
        prediction_array = model.predict(prediction_df)

        print(prediction_array)
        return

    def write_results(self):
        pass

    def plot(self):
        pass

    def full(self):
        # self.read_data()
        model_mnl = self.estimation_mnl()
        model_asym = self.estimation_asym(model_mnl)

        self.forecast(model_asym)
        # self.write_results()

        # self.plot()
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
    elif arg == 'estimate':
        conditional_mnl.estimation_mnl()
    elif arg == 'plot':
        conditional_mnl.plot()
    elif arg == "all":
        conditional_mnl.full()

    print(datetime.now() - start_time)