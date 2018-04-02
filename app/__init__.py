import pymysql
""" from util.DBUtils.PersistentDB import PersistentDB """
from util.DBUtils.PersistentDB import PersistentDB
from flask import Flask
from flask_compress import Compress
from app.config import Config


conf = Config()
compress = Compress()

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="../static"
)

app.config['THREADED'] = True
app.config['SECRET_KEY'] = conf.read_key('server', 'secret_key')
app.config['DEBUG'] = conf.read_key('server', 'debug')

app.config['COMPRESS_MIMETYPES'] = conf.read_section('mimetypes')

import app.routes as routes


def connect_db():
    """ Persistent connection for high concurrency """
    return PersistentDB(
        creator=pymysql, host=conf.read_key('mysqld', 'host'),
        user=conf.read_key('mysqld', 'user'), password=conf.read_key('mysqld', 'pass'),
        database=conf.read_key('mysqld', 'db'), autocommit=True,
        charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor
    )


def get_db():
    """ Opens a new connection per app """
    if not hasattr(app, 'db'):
        app.db = connect_db()

    return app.db.connection()


compress.init_app(app)
app.jinja_env.cache = {}
