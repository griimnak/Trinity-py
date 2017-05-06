from flask import Flask
from flask_socketio import SocketIO
try:
    from build import settings
except:
    setup = input('\n [NOTICE] Configuration not found, enter setup? (y/n)')
    if setup == 'n':
        print(' * Setup aborted, exiting..')
        exit()
    elif setup == 'y':
        print(' * Entering setup..\n\n')
        from build import installer
    else:
        print('"'+setup+'" is not an option, exiting..')
        exit()

# Set flask application properties
app = Flask(
    __name__,
    template_folder="views/{}/".format(settings.site['site_tpl']),
    static_folder="views/{}/static".format(settings.site['site_tpl'])
)

app.config['SECRET_KEY'] = settings.server['server_skey']
app.config['THREADED'] = True
app.config['DEBUG'] = settings.server['server_debug']
socketio = SocketIO(app)

from build.controllers import *
