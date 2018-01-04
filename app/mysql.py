import time
import pymysql
from app.config import Config
import threading


""" Create database instance
"""
def instance():
    conn = None

    try:
        conn = pymysql.connect(
            Config.read_key('mysqld', 'host'),
            Config.read_key('mysqld', 'user'),
            Config.read_key('mysqld', 'pass'),
            Config.read_key('mysqld', 'db')
        )
    except Exception as error:
        throw_connection_failed_error(str(error))
    return conn

def throw_connection_failed_error(error):
    print(' [NOTICE] Database connection failed: {}'.format(error))
