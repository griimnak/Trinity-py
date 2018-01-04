from flask import request, session
from pymysql import escape_string as clean
from passlib.hash import sha256_crypt as hasher
from app import get_db

class Login():
    def __init__(self, username, password):
        self.error = None
        self.verification = False

        self.username = clean(username)
        self.password = clean(password)
        
        self.locate_user_data()

    def locate_user_data(self):
        cursor = get_db().cursor()

        """ Check if requested user exists
        """
        sql = "SELECT username from users WHERE username = (%s);"
        if cursor.execute(sql, (self.username)):
            """ Fetch real password if requested user is found,
                export for comparison with verify_login(password)
            """
            sql2 = "SELECT password FROM users WHERE username =(%s);"
            if cursor.execute(sql2, (self.username)):
                row = cursor.fetchone()
                self.passw = row["password"]

                self.verify_login()
        else:
            self.error = 'The user you entered doesn\'t exist in our database.'

        cursor.close()
            
    def verify_login(self):
        """ Compare passwords
        """
        verify = hasher.verify(self.password, clean(self.passw))

        if verify is True:
            """ Begin session and send verification signal to
                controller if verify is True
            """
            session['username'] = self.username
            session['logged_in'] = True
            self.verification = True
        else:
            self.error = 'Incorrect password for ' + self.username

