import time
import configparser
import pymysql


class Database:
    def connect(self):

        config = configparser.ConfigParser()
        config.read('config.ini')

        try:
            self.conn = pymysql.connect(
                config['mysqld']['host'],
                config['mysqld']['user'],
                config['mysqld']['pass'],
                config['mysqld']['db']
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