from app import app
from app import conf

"""
 Trinity-py build tr4.4
 A python-based content management system using flask,
 pymysql, passlib-argon2 and ujson

 Note: local_server.py is not suitable for production, only for development.
 Please refer to readme.md for more info
"""


app.run(conf.read_key('server', 'host'), port=conf.read_key('server', 'port'))
