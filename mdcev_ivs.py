#!/usr/bin/python

# Local library imports
from mdcev.settings import *

# Python imports
from datetime import datetime
import sys
import subprocess


class ModelRun(object):

    def read_the_data(self):
        return

    def estimation(self):
        return

    def forecast(self):
        return

    def plot(self):
        return

    def full(self):
        self.read_the_data()
        self.estimation()
        self.forecast()
        self.plot()
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






