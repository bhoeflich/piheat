import time
import datetime as dt

from ControlMea import ControlMea
from ControlData import ControlData

measure_process = True
start_day = dt.datetime.now()

# init of classes
measure_controller = ControlMea()

data_controller = ControlData()
data_controller.initialize_csv()

while measure_process:
    temp_lst = measure_controller.get_temp()
    crit_sensors_data = measure_controller.check_temp(temp_lst)
    print(temp_lst[1])
    print(crit_sensors_data)

    data_controller.set_datapoint(temp_lst)

    # temp control structure
    if crit_sensors_data[0]:
        measure_controller.warn_temp(crit_sensors_data[2])
        measure_process = False


    actual_day = dt.datetime.now()

    if actual_day - start_day >= dt.timedelta(seconds=measure_controller.report_interval):

        plot_path = data_controller.create_plot(measure_controller.max_temp)
        print(plot_path)
        measure_controller.report_temp(plot_path)

        start_day = actual_day
        data_controller.new_file()
        data_controller.initialize_csv()

    time.sleep(measure_controller.interval)






