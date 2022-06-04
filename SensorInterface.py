import constants

# interface between sensors connected to pi and ControlMea

class SensorInterface:

    def __init__(self):
        self.paths = CON.SENSOR_PATHS
        self.factor = CON.TEMP_FACTOR
        self.raw_string = self.get_content()

    def get_content(self):
        raw_string = []

        for path in self.paths:
            with open(path, 'r') as file_txt:
                raw_string.append(file_txt.read())

        return raw_string

    def get_temperatures(self):
        temp_lst = []

        for string in  self.raw_string:
            temp_str = string.split('\n')[1].split(' ')[9]
            temp = float(temp_str[2:])/1000
            temp_lst.append(temp)

        return temp_lst
