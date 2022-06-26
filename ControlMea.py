import constants as CON
from SensorInterface import SensorInterface
from ControlNotify import ControlNotify



class ControlMea:

    def __init__(self):
        self.interval = CON.INTERVAL
        self.sensors = CON.SENSORS
        self.max_temp = CON.MAX_TEMP
        self.report_interval = CON.REP_INTERVAL

        self.interface = SensorInterface()
        self.notifier = ControlNotify()

    def __str__(self):
        return f'[interv:{self.interval}\n ' \
               f'amt senors:{self.sensors}\n ' \
               f'max temp:{self.max_temp}\n ' \
               f'report interv:{self.report_interval}]'

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

    def warn_temp(self, critical_temp):
        self.notifier.send_warning(critical_temp)

    def report_temp(self, plot_path='/plots/ups.png'):
        self.notifier.send_report(plot_path)



