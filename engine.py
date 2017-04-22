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

from multiprocessing import Process
from build import app
from build import settings
from build import database
from build import install
#---------------------------------------------\
# Check if configuration has been set.
#---------------------------------------------/
if settings.mysql['db_user'] == '' or settings.mysql['db_pass'] == '' or settings.mysql['db_host'] == '' or settings.mysql['db_name'] == '':
	print (' [NOTICE] Configuration has not been set! (build/settings.py)')
else:
	print (' * Loading config.. \n * Selecting db: ' + settings.mysql['db_name'])

database.validateConnection()
install.checkInstall()

def serveThreadedInstance():
		app.run('0.0.0.0', port=settings.server['server_port'], threaded=True)

plist = list()
p = Process(target=serveThreadedInstance())
p.start()
plist.append(p)
for p in plist:
	p.join()
