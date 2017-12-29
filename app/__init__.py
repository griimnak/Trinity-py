import configparser
from flask import Flask, url_for
from flask_compress import Compress

config = configparser.ConfigParser()
config.read('config.ini')

compress = Compress()

app = Flask(
    __name__,
    template_folder="views/",
    static_folder="../static"
)

app.config['SECRET_KEY'] = config['server']['secret_key']
app.config['THREADED'] = True
app.config['DEBUG'] = config['server']['debug']

import routes

compress.init_app(app)
app.jinja_env.cache = {}


