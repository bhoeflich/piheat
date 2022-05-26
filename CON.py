import os
# SYSTEM CONSTANTS

# Path of Sensor Data

SENSOR_PATHS = (os.path.abspath('../test_files/w1_slave.txt'), os.path.abspath('test_files/w2_slave.txt'),
                os.path.abspath('test_files/w3_slave.txt')
                )


# ControlMea
INTERVAL = 10                   # measuring interval in seconds
SENSORS = len(SENSOR_PATHS)     # amount of sensors used
MAX_TEMP = 60                   # maximum temp in degree celsius
REP_INTERVAL = 3                # report interval in days

#SensorInterface
TEMP_FACTOR = 1000              # factor as divisor to get the right temperatures
