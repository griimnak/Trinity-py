import ujson
""" A class for reading and interacting with 
    the configuration file
"""


class Config:
    def __init__(self):

        self.config = 'config.json'
        try:
            with open(self.config, 'r') as json_data_file:
                self.buffer = ujson.load(json_data_file)

        except Exception as e:
            raise ValueError('Trinity3 failed to initialize. ' + str(e))

    def read_key(self, section, key):
        return self.buffer[section][key]

    def read_section(self, section):
        data = self.buffer[section]

        for item in data:
            return ', '.join(data)

    def update_key(self, section, key, value):
        self.buffer[section][key] = value

        with open(self.config, 'w') as json_data_file:
            ujson.dump(self.buffer, json_data_file, indent=4)

    def add_section(self, section):
        self.buffer[section] = section

        with open(self.config, 'w') as json_data_file:
            ujson.dump(self.buffer, json_data_file, indent=4)

    def add_key(self, section, key, value):
        self.buffer[section][key] = value

        with open(self.config, 'w') as json_data_file:
            ujson.dump(self.buffer, json_data_file, indent=4)

    def remove_key(self, section, key):
        return 'To do'
