#!/usr/bin/env python
import os
import time
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
           Trinity 3, for Python 3.6.x    \/__/  
A Python-based Content Management System originally designed for Habbo private servers.
Written by griimnak. Project inspired by Kyle Greene & Chris Pettyjohn
''')

from build import installer
from build import app, socketio

print(' * Loading config..')
from build import settings

import build.database as database
database.validate_connection()
print(' * Selecting db: ' + settings.mysql['db_name'])

if __name__ == '__main__':
    print(' * Binding to: {}:{}..'.format(str(settings.server['server_host']), str(settings.server['server_port'])))
    try:
        print('\n * Trinity 3 -> LOADED! in {} seconds'.format(time.time() - stop_watch))
        socketio.run(app, host='0.0.0.0', port=settings.server['server_port'], debug=settings.server['server_debug'])
    except Exception as e:
        print(' [NOTICE] Unexpected error occurred: ' + str(e))
        exit()
