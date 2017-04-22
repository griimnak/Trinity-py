from flask import Flask
try:
	from build import settings
except:
	setup = input('\n [NOTICE] Configuration not found, enter setup? (y/n)')
	if setup == 'n':
		print(' * Setup aborted, exiting..')
		exit()
	elif setup == 'y':
		print(' * Entering setup..\n\n')
		from build import install
		install.install_settings()
	else:
		print('"'+setup+'" is not an option, exiting..')
		exit()	

#---------------------------------------------\
# Set flask application properties
#---------------------------------------------/
app = Flask('build', template_folder="views/", static_folder="views/static")
app.config['SECRET_KEY'] = settings.server['server_skey']
app.config['THREADED'] = True
app.config['DEBUG'] = settings.server['server_debug'] 

from build.controllers import *
