import csv
import pandas as pd
import datetime as dt

# controles the data management
# To Do
# - header has to be parametric depending on CON.SENSORS
# - set datapoint has to be parametric depending on CON.SENSORS


class ControlData:

    def __init__(self):
        self.timestamp = dt.datetime.now().replace(microsecond=0)
        self.__filepath = 'data/'
        self.filename = 'temp-data-' + str(dt.date.today()) + '.csv'

        self.current_file = 'data/' + 'temp-data-' + str(dt.date.today()) + '.csv'



    def initialize_csv(self):

        with open(self.current_file, 'x', newline='') as temp_data_file:
            writer = csv.writer(temp_data_file, delimiter=',')
            writer.writerow(['timestamp', 'temp1', 'temp2', 'temp3'])

    def set_filepath(self, new_path):
        self.__filepath = new_path

    def set_datapoint(self, temp_lst):
        with open(self.current_file, 'a', newline='') as temp_data_file:
            writer = csv.writer(temp_data_file, delimiter=',')
            writer.writerow([self.timestamp, temp_lst[0], temp_lst[1], temp_lst[2]])
