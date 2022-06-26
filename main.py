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
    temp_lst = measure_controller.get_temp()
    crit_sensors_data = measure_controller.check_temp(temp_lst)
    print(temp_lst)
    print(crit_sensors_data)

    data_controller.set_datapoint(temp_lst)

    # temp control structure
    if crit_sensors_data:
        measure_controller.warn_temp(crit_sensors_data[3])
        measure_process = False
        pass

    actual_day = dt.date.today()

    if actual_day - start_day >= dt.timedelta(days=measure_controller.report_interval):
        measure_controller.report_temp(data_controller.create_plot())
        start_day = actual_day
        pass

    time.sleep(measure_controller.interval)






