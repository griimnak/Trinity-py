import pymysql
from DBUtils.PersistentDB import PersistentDB

from trinity import Trinity

from app.configs.config import config
from app.configs.routes import urls


app = Trinity(
    routes=urls,
    tpl_dir="templates"
)


def connect_db():
    return PersistentDB(
        creator=pymysql,
        host=config['mysql']['host'],
        user=config['mysql']['user'],
        password=config['mysql']['passw'],
        database=config['mysql']['database'],
        autocommit=True,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

def get_db():
    if not hasattr(app, 'db'):
        app.db = connect_db()

    return app.db.connection()
