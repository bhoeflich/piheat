import time
import datetime as dt

from ControlMea import ControlMea
from ControlData import ControlData

measure_process = True
start_day = dt.date.today()

# init of classes
measure_controller = ControlMea()

data_controller = ControlData()
data_controller.initialize_csv()

while measure_process:
    time.sleep(measure_controller.interval)

    temp_lst = measure_controller.get_temp()
    crit_sensors_data = measure_controller.check_temp(temp_lst)
    print(temp_lst)
    print(crit_sensors_data)

    data_controller.set_datapoint(temp_lst)

    # temp control structure
    if crit_sensors_data:
        # measure_controller.warn_temp()
        measure_process = False
        pass

    actual_day = dt.date.today()

    if actual_day - start_day >= dt.timedelta(days=measure_controller.report_interval):
        # measure_controller.report_temp()
        start_day = actual_day
        pass








