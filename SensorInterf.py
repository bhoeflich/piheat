import CON


class SensorInterface:

    def __init__(self):
        self.paths = CON.SENSOR_PATHS
        self.factor = CON.TEMP_FACTOR
        self.raw_string = self.get_content()
        self.temp_container = self.get_temperatures()

    def get_content(self):
        raw_string = []

        for path in self.paths:
            with open(path, 'r') as file_txt:
                raw_string.append(file_txt.read())

        return raw_string

    def get_temperatures(self):
        temp_container =

        for string in self.raw_string:


        pass

intef_test = SensorInterface()
print(intef_test.raw_string)
