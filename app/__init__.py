from flask import Flask
from flask_socketio import SocketIO

import app.Settings

app = Flask(
    __name__,
    template_folder="views/",
    static_folder="views/static"
)

app.config['SECRET_KEY'] = Settings.server['server_skey']
app.config['THREADED'] = True
app.config['DEBUG'] = Settings.server['server_debug']
socketio = SocketIO(app)

from app.controllers import *
