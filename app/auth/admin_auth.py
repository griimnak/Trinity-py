from flask import request, session
from pymysql import escape_string as clean
from passlib.hash import argon2 as hasher
from app import get_db


class Login:
    def __init__(self, username, password):
        self.error = None
        self.verification = False
        self.username = clean(username)
        self.password = clean(password)

        self.locate_user_data()

    def locate_user_data(self):
        cursor = get_db().cursor()
        sql = "SELECT username from users WHERE username = (%s);"

        """ Check if requested user exists """
        if cursor.execute(sql, self.username):
            sql2 = "SELECT password FROM users WHERE username =(%s);"

            """ Fetch real password if requested user is found,
                export for comparison with verify_login(password)
            """
            if cursor.execute(sql2, self.username):
                row = cursor.fetchone()
                genuine_pass = row["password"]

                self.verify_login(genuine_pass)
        else:
            self.error = 'The user you entered doesn\'t exist in our database.'

        cursor.close()
            
    def verify_login(self, genuine_pass):
        """ Compare passwords """
        verify = hasher.verify(self.password, clean(genuine_pass))

        if verify is True:
            """ Begin session and send verification signal to
                controller if verify is True
            """
            session['username'] = self.username
            session['logged_in'] = True
            self.verification = True
        else:
            self.error = 'Incorrect password for ' + self.username

