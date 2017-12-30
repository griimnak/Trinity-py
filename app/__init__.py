from app.config import Config
from flask import Flask, url_for
from flask_compress import Compress

compress = Compress()

app = Flask(
    __name__,
    template_folder="views/",
    static_folder="../static"
)

app.config['SECRET_KEY'] = Config.read_key('server', 'secret_key')
app.config['THREADED'] = True
app.config['DEBUG'] = Config.read_key('server', 'debug')

import routes

from app.middlewares import *

compress.init_app(app)
app.jinja_env.cache = {}


