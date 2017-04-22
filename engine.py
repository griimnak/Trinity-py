#!/usr/bin/env python
import os
os.system('cls' if os.name == 'nt' else 'clear')
print ('''
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

#---------------------------------------------\
# Check if required modules are installed.
#---------------------------------------------/
import apis

from build import app
from build import install
#---------------------------------------------\
# Check if configuration has been set.
#---------------------------------------------/
try:
  from build import settings
except:
	setup = input('\n [NOTICE] Configuration not found, enter setup? (y/n)')
	if setup == 'n':
		print(' * Setup aborted, exiting..')
		exit()
	elif setup == 'y':
		print(' * Entering setup..\n\n')
		install.install_settings()
	else:
		print('"'+setup+'" is not an option, exiting..')
		exit()
else:
	from build import settings
	print (' * Loading config.. \n * Selecting db: ' + settings.mysql['db_name'])

from build import database
database.validate_connection()
install.install_database()

if __name__ == '__main__':
  app.run('0.0.0.0', port=settings.server['server_port'], threaded=True)