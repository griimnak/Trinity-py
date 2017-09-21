#!/usr/bin/env python
import os
import time
from app import app, socketio, Settings
import Routes
from lib.Database import Database

# GUNICORN
from werkzeug.contrib.fixers import ProxyFix

__name__ = 'Trinity'
__version__ = '3.1.0'
__author__ = 'griimnak'

stop_watch = time.time()
os.system('cls' if os.name == 'nt' else 'clear')
print('''
 ______                       __                   __     
/\__  _\       __          __/\ \__              /'__`\   
\/_/\ \/ _ __ /\_\    ___ /\_\ \ ,_\  __  __    /\_\L\ \  
   \ \ \/\`'__\/\ \ /' _ `\/\ \ \ \/ /\ \/\ \   \/_/_\_<_ 
    \ \ \ \ \/ \ \ \/\ \/\ \ \ \ \ \_\ \ \_\ \    /\ \L\ \        
     \ \_\ \_\  \ \_\ \_\ \_\ \_\ \_\ \/`____ \   \ \____/
      \/_/\/_/   \/_/\/_/\/_/\/_/\/__/ `/___/> \   \/___/ 
                                          /\___/          
           Trinity 3, for Python 3.2+     \/__/  
 /=============================================================\ 
 | A Python-based Content Management System originally         |
 | designed for Habbo private servers.                         |
 |                                                             |
 | Written by griimnak.                                        |
 | Project idea inspired by Kyle Greene & Chris Pettyjohn      |
 \=============================================================/

''')

print(' * Selecting db: ' + Settings.mysql['db_name'])
db = Database()
db.validate()

# GUNICORN
app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == 'Trinity' and __author__ == 'griimnak':
    print(' * Binding..')
    try:
        print(
            '\n * Trinity 3 -> LOADED! in {} seconds'
            .format(time.time() - stop_watch)
        )

        app.jinja_env.cache = {}

        socketio.run(
            app,
            host='0.0.0.0',
            port=Settings.server['server_port'],
            debug=Settings.server['server_debug']
        )
    except Exception as e:
        print(' [NOTICE] Unexpected error occurred: ' + str(e))
        exit()
else:
    exit("\n beep boop *self destructing*")
