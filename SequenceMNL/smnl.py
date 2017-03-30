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

    def __init__(self):
        self.data = Data(source_file=self.original_source_file,
                         output_file=self.output_file)

    # read the data
    def read_data(self):
        flag = self.data.read_sequence()
        print("This is the data", flag)

        return flag

    # Estimation
    def estimation(self):
        pass

    # Simulation
    def forecast(self):
        pass

    # Reform results
    def write_results(self):
        pass

    # Compare the results to the data and plot
    def plot(self):
        pass

    def full(self):
        self.read_data()
        self.estimation()
        self.forecast()
        self.write_results()
        self.plot()
        print("This is a FULL run")
        pass


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

    # elif arg == 'coef':
    #     smnl._get_coef()

    elif arg == 'forecast':
        smnl.forecast()

    elif arg == 'plot':
        smnl.plot()

    elif arg == 'all':
        smnl.full()

    print(datetime.now() - start_time)




