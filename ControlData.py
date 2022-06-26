import csv
import datetime

import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
import  time


# todo header has to be parametric depending on CON.SENSORS
# todo datapoint has to be parametric depending on CON.SENSORS
# todo after testing remove datetime.now() form new_file


class ControlData:

    def __init__(self):
        self.__filepath = 'data/'
        # self.filename = 'temp-data-' + str(dt.date.today()) + '.csv'
        self.csv_path = self.__filepath + 'temp-data-' + str(dt.datetime.now()) + '.csv'

        self.plot_path = 'plots/report_plot-' + str(dt.date.today()) + '.png'
        self.html_plot_path = '/' + 'plots/report_plot-' + str(dt.date.today()) + '.png'

    def new_file(self):
        self.csv_path = self.__filepath + 'temp-data-' + str(dt.datetime.now()) + '.csv'

    def set_filepath(self, new_path):
        self.__filepath = new_path

    def initialize_csv(self):
        with open(self.csv_path, 'x', newline='') as temp_data_file:
            writer = csv.writer(temp_data_file, delimiter=',')
            writer.writerow(['timestamp', 'temp1', 'temp2', 'temp3'])

    def set_datapoint(self, temp_lst):
        with open(self.csv_path, 'a', newline='') as temp_data_file:
            writer = csv.writer(temp_data_file, delimiter=',')
            writer.writerow([dt.datetime.now().replace(microsecond=0), temp_lst[0], temp_lst[1], temp_lst[2]])

    def create_plot(self, max_temp):
        plot_data = pd.read_csv(self.csv_path, index_col='timestamp')

        fig, ax = plt.subplots(figsize=(15, 15))
        ax.plot(plot_data.index, plot_data.temp1)
        ax.plot(plot_data.index, plot_data.temp2)
        ax.axhline(max_temp, color='red')

        ax.tick_params(axis='x', labelrotation=90)

        ax.set_title('Temperaturen des letzten Intervalls', size=20)
        ax.set_ylabel('Temperatur [°C]', size=15)
        # ax.set_xlabel('Zeit', size=15 )
        fig.show()
        fig.savefig(self.plot_path)

        plot_path = self.html_plot_path
        return plot_path

