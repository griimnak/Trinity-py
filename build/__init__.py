from flask import Flask
from build import settings

#---------------------------------------------\
# Set flask application properties
#---------------------------------------------/
app = Flask('build', template_folder="views/", static_folder="views/static")
app.config['SECRET_KEY'] = settings.server['server_skey']
app.config['THREADED'] = True
app.config['DEBUG'] = settings.server['server_debug'] 

from build.controllers import *
