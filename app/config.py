import threading  
import configparser

""" A class for reading and interacting with 
    the configuration file
    
    (trying threading for non blocking config read)
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

def read_config_threaded():
    return Config()

""" If threading is breaking the app try
    removing the lines below and replacing them with:
    Config()
"""
t = threading.Thread(target=read_config_threaded)

if t.isAlive():
    print('[DEBUG] Thread is alerady opened')
else:
    t.start()