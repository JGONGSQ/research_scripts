#!/usr/bin/python
import sys
sys.path.append('../')
import subprocess
import math
from datetime import datetime


# Local imports
from settings import *
from SequenceMNL.extensions import Data


# Python imports


class ModelRun(object):



    # R script
    r_estimation = "r/duration_estimation_prediction.r"

    # csv files
    original_source_file = '../../Data/test_output_file.csv'
    output_file = "../../data/linear_regression_output.csv"
    forecast_results_file = "../../data/linear_regression_forecast.csv"

    # packages
    data = Data(source_file=original_source_file,
                output_file=output_file,
                forecast_file=forecast_results_file)

    # read the data
    def read_the_data(self):
        pass

    # estimation and forecast
    def estimation(self):
        process = subprocess.call(
            ['Rscript --vanilla {r_script}'.format(r_script=self.r_estimation)]
            , shell=True)
        return

    # evalutate
    def evaluation(self):
        # initial value
        forecast_index = 0
        origin_index = 0
        sub_total = 0.0

        # read the files
        forecast_results = self.data.read(filepath=self.forecast_results_file)
        source = self.data.read(filepath=self.original_source_file)

        # calculate line residual line by line
        for i,  line in enumerate(forecast_results):
            if i == 0:
                forecast_index = line.index('results')
                origin_index = source[i].index('Duration')

            else:
                # might need to think about round method, but keep it like this for now
                sub_total += (float(source[i][origin_index]) - round(float(line[forecast_index]),0)) ** 2

        print("This is the subtotal", sub_total, len(forecast_results))
        rmse = math.sqrt(sub_total/len(forecast_results))

        print("This is the RMSE value for linear regression", rmse)

        return

    # plot
    def plot(self):
        pass

    # full run
    def full(self):
        self.read_the_data()
        self.estimation()
        self.evaluation()
        self.plot()
        print("This is a FULL run")
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

    elif arg == 'plot':
        model_run.plot()

    elif arg == 'all':
        model_run.full()

    print(datetime.now() - start_time)