#!/usr/bin/python
# Local library imports

# python imports
import sys
import subprocess
from datetime import datetime


class SequenceMNL(object):


    # csv data files

    # Get the data
    def get_data(self):
        pass

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
        self.get_data()
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
        smnl.get_data()

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




