#!/usr/bin/python
# Local library imports
from settings import *
from extensions import Data

# python imports
import sys
import subprocess
from datetime import datetime


class SequenceMNL(object):
    # R script
    r_estimation = RUNNER_SMNL

    # csv data files
    original_source_file = SOURCE_INPUT_FILE
    output_file = OUTPUT_FILE
    forecast_file = FORECAST_FILE

    def __init__(self):
        self.data = Data(source_file=self.original_source_file,
                         output_file=self.output_file,
                         forecast_file=self.forecast_file)

    # read the data
    def read_data(self):
        sequence_data = self.data.sequence()
        self.data.write(sequence_data)
        return

    # Estimation
    def estimation(self):
        # run the estimation in R script file
        process = subprocess.call(
            ['Rscript --vanilla {r_script}'.format(r_script=self.r_estimation)]
            , shell=True)
        return

    # Simulation
    def forecast(self):
        # some python script to call the forecast function
        pass

    # Reform results
    def write_results(self):
        pass

    # Compare the results to the data and plot
    def plot(self):
        self.data.compare()

        return

    def full(self):
        self.read_data()
        self.estimation()
        self.forecast()
        self.write_results()
        self.plot()
        print("This is a FULL run")
        return


if __name__ == '__main__':
    smnl = SequenceMNL()
    start_time = datetime.now()

    argv = sys.argv

    try:
        arg = argv[1]
    except Exception:
        arg = 'all'

    if arg == 'read':
        smnl.read_data()

    elif arg == 'estimation':
        smnl.estimation()

    elif arg == 'forecast':
        smnl.forecast()

    elif arg == 'plot':
        smnl.plot()

    elif arg == 'all':
        smnl.full()

    print(datetime.now() - start_time)




