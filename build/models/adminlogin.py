from flask import request, session
from passlib.hash import sha256_crypt as hasher
import build.database as database
from pymysql import escape_string as clean


class Login(object):
    def __init__(self):
        self.error = None
        self.verification = False
        # POST trigger
        if request.method == 'POST':
            self.username = clean(str(request.form['username']))
            self.password = clean(str(request.form['password']))

            # Check if fields have been left blank
            if self.username == '' or self.password == '':
                self.error = 'One or more fields have been left blank.'
            else:
                # Begin querying database
                self.locate_user_data()

    def locate_user_data(self):
        # Attempt to select user in database as @self.username
        try:
            database.instance.execute("SELECT COUNT(1) FROM trinity_users WHERE username = %s;", [self.username])
            if database.instance.fetchone()[0]:
                # Select corresponding password for comparison if user is found
                database.instance.execute("SELECT password FROM trinity_users WHERE username = %s;", [self.username])
                for row in database.instance.fetchall():
                    self.passw = row[0]
                self.verify_login()
            else:
                self.error = 'The user you entered doesn\'t exist in our database.'
        except Exception as e:
            print(' 500 ERROR: ' + str(e))

    def verify_login(self):
        # Compare inputted password with queried one
        verify = hasher.verify(self.password, clean(self.passw))

        if verify is True:
            # Begin sessions and verify
            session['username'] = self.username
            session['logged_in'] = True
            self.verification = True
        else:
            self.error = 'Incorrect password for ' + self.username
Login()
