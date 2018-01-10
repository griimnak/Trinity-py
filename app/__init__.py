from app.config import Config
import pymysql
from app.__trinity__.csrf_system import generate_csrf_token
from flask import Flask, url_for, render_template
from flask_compress import Compress
from util.DBUtils.PersistentDB import PersistentDB
import json
import sys

cfg = Config()
compress = Compress()

app = Flask(
    __name__,
    template_folder="views/",
    static_folder="../pub"
)

app.config['SECRET_KEY'] = cfg.read_key('server', 'secret_key')
app.config['THREADED'] = True
app.config['DEBUG'] = cfg.read_key('server', 'debug')

mimetypes = [
'text/html', 
'text/css', 
'text/xml', 
'application/json',
'application/javascript',
'image/jpeg',
'image/png',
'image/gif',
'text/javascript'
]

app.config['COMPRESS_MIMETYPES'] = mimetypes

@app.route('/', defaults={'path': ''})
@app.route('/<path>')
def index(path):
    data = {
        "site": {
            "name": cfg.read_key('site', 'name'),
            "desc": cfg.read_key('site', 'desc'),
            "port": cfg.read_key('server', 'port')
        },
        "pyinfo": sys.version
    }

    return render_template(
       'index.html',
       data=data,
       csrf_token=generate_csrf_token()
    )

from app.middlewares import *

def connect_db():
    """ Persistent connection for high concurrency
        (nearly ~30% faster than per request!)
    """
    return PersistentDB(
        creator = pymysql,
        host = cfg.read_key('mysqld', 'host'),
        user = cfg.read_key('mysqld', 'user'), 
        password = cfg.read_key('mysqld', 'pass'), 
        database = cfg.read_key('mysqld', 'db'), 
        autocommit = True, 
        charset = 'utf8mb4', 
        cursorclass = pymysql.cursors.DictCursor
    )

def get_db():
    """ Opens a new database connection per app.
    """
    if not hasattr(app, 'db'):

        app.db = connect_db()
    return app.db.connection() 

compress.init_app(app)
app.jinja_env.cache = {}


