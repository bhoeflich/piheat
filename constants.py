import os
import datetime as dt


# SYSTEM CONSTANTS

# Path of Sensor Data
SENSOR_PATHS = ('/sys/bus/w1/devices/28-1de3851e64ff/w1_slave',
                '/sys/bus/w1/devices/28-1de3851e64ff/w1_slave',
                '/sys/bus/w1/devices/28-1de3851e64ff/w1_slave'
                )

# ControlMea
INTERVAL = 60                   # measuring interval in seconds
SENSORS = len(SENSOR_PATHS)     # amount of sensors used
MAX_TEMP = 60                   # maximum temp in degree celsius
REP_INTERVAL = 3                # report interval in days

# SensorInterface
TEMP_FACTOR = 1000              # factor as divisor to get the right temperatures

# Notify
EMAIL = 'piheat.alert@hotmail.com'
PASSWORD = 'PiHeat!2Hot'
SMTP_SERVER = 'smtp.office365.com'
SMTP_PORT = '587'

# Servername: smtp.office365.com
# Port: 587
# Verschlüsselungsmethode: STARTTLS

