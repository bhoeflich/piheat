import CON


class ControlMea:

    def __init__(self):
        self.interval = CON.INTERVAL
        self.sensors = CON.SENSORS
        self.max_temp = CON.MAX_TEMP
        self.report_interval = CON.REP_INTERVAL

    def __str__(self):
        return f'[interv:{self.interval}\namt senors:{self.sensors}\nmax temp:{self.max_temp}\nreport interv:{self.report_interval}]'

    def get_temp(self):
        # makes an instance of SensorInterface when it is called
        pass
        # return temp_lst

    def check_temp(self, temp_lst):
        crit_temp = 0
        crit_sensor = None
        crit_bool = False

        for idx, value in temp_lst:
            if value >= self.max_temp:
                crit_temp = value
                crit_sensor = idx

        return crit_bool, crit_sensor, crit_temp

    def warning_temp(self):
        pass

    def report_temp(self):
        pass






# test = ControlMea()

