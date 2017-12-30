import time
from app.config import Config
import pymysql


class Database:
    def connect(self):
        try:
            self.conn = pymysql.connect(
                Config.read_key('mysqld', 'host'),
                Config.read_key('mysqld', 'user'),
                Config.read_key('mysqld', 'pass'),
                Config.read_key('mysqld', 'db')
            )

        except (AttributeError, pymysql.OperationalError) as e:
            raise e

    def query(self, sql, params = ()):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, params)
        except (AttributeError, pymysql.OperationalError) as e:
            print(' * MySQL -> Exception generated during sql query: ', e)
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql, params)
        return cursor

    def close(self):
        try:
            if self.conn:
                self.conn.close()
                print(' * MySQL -> Closed connection: ' + str(self.conn))
            else:
                print(' * MySQL -> Ignoring close() request.')
        except (AttributeError, pymysql.OperationalError) as e:
            raise e

    def validate(self):
        try:
            self.connect()
            print(' * Database connected successfully!')
        except Exception as e:
            exit(' * Database connection failed. ' + str(e))

        self.close()