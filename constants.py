import os
import datetime as dt


# SYSTEM CONSTANTS

# Path of Sensor Data
SENSOR_PATHS = ('/Users/bjoernhoefer/Desktop/SOM/piheat/test_files/w1_slave.txt',
                '/Users/bjoernhoefer/Desktop/SOM/piheat/test_files/w2_slave.txt',
                '/Users/bjoernhoefer/Desktop/SOM/piheat/test_files/w3_slave.txt'
                )



# ControlMea
INTERVAL = 10                   # measuring interval in seconds
SENSORS = len(SENSOR_PATHS)     # amount of sensors used
MAX_TEMP = 60                   # maximum temp in degree celsius
REP_INTERVAL = 3                # report interval in days

# SensorInterface
TEMP_FACTOR = 1000              # factor as divisor to get the right temperatures


# Notify
EMAIL = 'piheat.alert@gmx.de'
PASSWORD = 'PiHeat!2Hot'
SMTP_SERVER = 'smtp.office365.com'
SMTP_PORT = '587'
REPORT_SUBJECT = 'Temperature Report {}'.format(dt.datetime.now().replace(microsecond=0))
REPORT_HTML = ' '
WARNING_SUBJECT = 'Temperature Warning {}'.format(dt.datetime.now().replace(microsecond=0))
WARNING_HTML = ' '
