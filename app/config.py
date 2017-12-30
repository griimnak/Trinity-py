import threading  
import configparser

""" A class for reading and interacting with 
    the configuration file
"""
class Config:
    def __init__(self):
        config = 'config.ini'
        self.parser = configparser.ConfigParser()
        self.parser.read(config)

    def read_key(section, key):
        return Config().parser[section][key]

    def update_key(section, key, value):
        return Config().parser.set(section, key, value)

    def add_section(section):
        return Config().parser.add_section(section)

    def add_key(section, key, value):
        return Confg().parser.add_option(section, key, value)

    def remove_key(section, key):
        return Confg().parser.remove_option(section, key)