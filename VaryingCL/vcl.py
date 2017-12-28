#!/usr/bin/python
from settings import *
from extensions import Data

import sys

import pandas as pd
import numpy as np


from datetime import datetime

### Code Start ###


class VCLogit(object):

    # csv data files
    original_source_file = SOURCE_INPUT_FILE
    output_file = OUTPUT_FILE
    forecast_file = FORECAST_FILE

    def __init__(self):
        self.data = Data(source_file=self.original_source_file,
                         output_file=self.output_file,
                         forecast_file=self.forecast_file)

    def read_data(self):
        conditional_data = self.data.vcl()
        self.data.write(conditional_data)
        return

if __name__ == '__main__':
    vclogit = VCLogit()
    start_time = datetime.now()

    argv = sys.argv
    try:
        arg = argvp[1]
    except Exception:
        arg = 'read'

    if arg == 'read':
        vclogit.read_data()

    print(datetime.now() - start_time)