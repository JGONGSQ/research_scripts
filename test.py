#!/usr/bin/python
import random, string
# Import the packagess
from py_files.data import *
from py_files.settings import *
from py_files.forecast import evaluate
from py_files.plot import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pylab
from datetime import datetime
import os
# import single_forecast
# import single_run_with_multiple_utility_model_estimation

start_time = datetime.now()
os.system("pythonw single_run_with_multiple_utility_model_estimation.py")
os.system("pythonw single_forecast.py")

print(datetime.now() - start_time)
