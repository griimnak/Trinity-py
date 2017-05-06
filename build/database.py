import time
import pymysql
from build import settings
import threading


# KeepAlive: [True | False]
# Pings MySQL every x seconds
KeepAlive = dict(
    Enabled=True,
    Duration=300
)


class _Handler:
    # Create database instance
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                settings.mysql['db_host'],
                settings.mysql['db_user'],
                settings.mysql['db_pass'],
                settings.mysql['db_name']
            )
        except Exception as error:
            self.throw_connection_failed_error(str(error))

    def throw_connection_failed_error(self, error):
        print(' [NOTICE] Database connection failed: {}'.format(error))
        exit()


def validate_connection():
    if _Handler().conn.open is False:
        print(' [NOTICE] Database connection failed.')
    else:
        print(' * Database connected successfully!')


def keep_connection_alive():
    while True:
        time.sleep(KeepAlive['Duration'])
        try:
            _Handler().conn.ping()
            print(' * KeepAlive -> Pinged MySQL')
        except(Exception, pymysql.OperationalError):
            print(' [NOTICE] Database connection died, reconnecting..')
            _Handler()
_Handler()

if KeepAlive['Enabled'] is True:
    t = threading.Thread(target=keep_connection_alive)
    t.start()

instance = _Handler().conn.cursor()
_Handler().conn.autocommit(True)

