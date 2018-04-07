from app import conf
from app import app
from os import system
system("title (DEV) [{}:{}] Trinity-py- build tr4.4".format(
    conf.read_key('server', 'host'), conf.read_key('server', 'port')))
system("color 3E")
""" 
 Trinity-py build tr4.4
 A python-based content management system using flask, pymysql, passlib and ujson
 
 Note: local_server.py is not suitable for production. It is only for development
 Please refer to readme.md for more info
"""


app.run(conf.read_key('server', 'host'), port=conf.read_key('server', 'port'))
