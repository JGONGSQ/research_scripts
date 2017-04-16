#!/usr/bin/python

# imports from local package
from settings import *

# python imports
import csv


class Data(object):

    def __init__(self, source_file, output_file, forecast_file, data=None):
        self.source_file = source_file
        self.output_file = output_file
        self.forecast_file = forecast_file
        self.data = data

    def read(self, filepath):
        self.data = list()

        with open(filepath, 'rU') as csvfile:
            file = csv.reader(csvfile, delimiter=',')
            for row in file:
                self.data.append(row)
            csvfile.close()

        return self.data

    def conditional_mnl(self):
        pass

    def write(self, data):

        try:
            with open(self.output_file, 'w') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')

                for row in data:
                    writer.writerow(row)

        except Exception as error:
            raise error

        return True

    def combine(self):
        pass

    def compare(self):
        pass
