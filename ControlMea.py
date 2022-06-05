import constants as CON
from SensorInterface import SensorInterface


class ControlMea:

    def __init__(self):
        self.interval = CON.INTERVAL
        self.sensors = CON.SENSORS
        self.max_temp = CON.MAX_TEMP
        self.report_interval = CON.REP_INTERVAL

        self.interface = SensorInterface()


    def __str__(self):
        return f'[interv:{self.interval}\namt senors:{self.sensors}\nmax temp:{self.max_temp}' \
               f'\nreport interv:{self.report_interval}]'

    def get_temp(self) -> list:
        return self.interface.get_temperatures()

    def check_temp(self, temp_lst):
        crit_temp = 0
        crit_sensor = None
        crit_bool = False

        for idx, value in enumerate(temp_lst):
            if value >= self.max_temp:
                crit_bool = True
                crit_temp = value
                crit_sensor = idx + 1
                break

        return crit_bool, crit_sensor, crit_temp

    def warning_temp(self):
        pass

    def report_temp(self):
        pass

    def set_datapoint(self):
        pass


