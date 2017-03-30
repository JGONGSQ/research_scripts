#!/usr/bin/python
import csv


class Data(object):
    # initial
    def __init__(self, source_file, output_file, data=None):
        self.source_file = source_file
        self.output_file = output_file
        self.data = data

    # read
    def read_sequence(self):
        print("12312313123")

        return self.data

    # write
    def write(self):
        """
            Write the results list to generate a new data file
        """
        # open the file need to be write
        try:
            with open(self.output_file, 'w') as csvfile:
                # initial the writer
                writer = csv.writer(csvfile, delimiter=',')

                # write each row
                for row in self.data:
                    writer.writerow(row)

        except Exception as error:
            print error
            return False

        return True

    # combine
    def combine(self):
        pass

    # compare
    def compare(self):
        pass




