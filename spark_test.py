#!/usr/bin/python
# import random, string
# Import the packagess
# from py_files.data import *
# from py_files.settings import *
# from py_files.forecast import evaluate
# from py_files.plot import *
# from datetime import datetime
# import os
# import single_forecast
# import single_run_with_multiple_utility_model_estimation
#
# start_time = datetime.now()
# os.system("pythonw single_run_with_multiple_utility_model_estimation.py")
# os.system("pythonw single_forecast.py")
#
# print(datetime.now() - start_time)

import findspark
findspark.init()

from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, BooleanType
from pyspark.sql.session import SparkSession


sc = SparkContext('local')
# words = sc.parallelize(["scala","java","hadoop","spark","akka"])
# print words.count()
spark = SparkSession(sc)

data = spark.read.csv('../Data/NVS2007unit.csv', header=True, inferSchema=True)

print(data.count())