import time
import datetime as dt

from ControlMea import ControlMea
from ControlData import ControlData
from Notify import Notify


measure_process = True

measure_controller = ControlMea()

data_controller = ControlData()
data_controller.initialize_csv()

start_day = dt.date.today()

while measure_process:
    time.sleep(measure_controller.interval)

    temp_lst = measure_controller.get_temp()
    crit_sensors_data = measure_controller.check_temp(temp_lst)
    print(temp_lst)
    print(crit_sensors_data)

    data_controller.set_datapoint(temp_lst)

    if crit_sensors_data:
        # Notify.send_warning()
        measure_process = False
        pass

    actual_day = dt.date.today()
    if actual_day - start_day >= dt.timedelta(days=measure_controller.report_interval):
        # Notify.send_report()
        start_day = actual_day
        pass








