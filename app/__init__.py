import configparser
from flask import Flask, url_for
from flask_compress import Compress
from werkzeug.contrib.cache import SimpleCache

config = configparser.ConfigParser()
config.read('config.ini')

compress = Compress()

app = Flask(
    __name__,
    template_folder="views/",
    static_folder="../static"
)

CACHE_TIMEOUT = 300
cache = SimpleCache()
class cached(object):
    def __init__(self, timeout=None):
        self.timeout = timeout or CACHE_TIMEOUT

    def __call__(self, f):
        def decorator(*args, **kwargs):
            response = cache.get(request.path)
            if response is None:
                response = f(*args, **kwargs)
                cache.set(request.path, response, self.timeout)
            return response
        return decorator

app.config['SECRET_KEY'] = config['server']['secret_key']
app.config['THREADED'] = True
app.config['DEBUG'] = config['server']['debug']

import routes

compress.init_app(app)
app.jinja_env.cache = {}


