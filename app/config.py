import threading  
import configparser

""" A class for reading and interacting with 
    the configuration file
"""
class Config:
    def __init__(self):
        self.config = 'config.ini'
        self.parser = configparser.ConfigParser()
        self.parser.read(self.config)

    def read_key(self, section, key):

        return self.parser[section][key]

    def update_key(self, section, key, value):

        return self.parser.set(section, key, value)

    def add_section(self, section):

        return self.parser.add_section(section)

    def add_key(self, section, key, value):

        return self.parser.add_option(section, key, value)

    def remove_key(self, section, key):

        return self.parser.remove_option(section, key)