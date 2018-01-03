from flask import request, session
from pymysql import escape_string as clean
from passlib.hash import sha256_crypt as hasher

class Login():
    def __init__(self):
        self.error = None
        self.verification = False

        """ Double check if the submit button was actually pressed.
            Extra security I guess,
        """
        if request.form['login-submit'] != None:
            self.username = clean(str(request.form['username']))
            self.password = clean(str(request.form['password']))

            """ Check if fields are blank
            """
            if self.username == '' or self.password == '':
                self.error = 'One or more fields have been left blank.'

            else:
                """ Query database if input is present
                """
                self.locate_user_data()
        else:
            return "What did you do?"

    def locate_user_data(self):
        try:
            import app.mysql as db

            db.instance.execute(
                "SELECT COUNT(1) FROM users WHERE username = %s;", 
                [self.username]
            )

            """ Find password for requested user if exists
            """
            if db.instance.fetchone()[0]:
                db.instance.execute(
                    "SELECT password FROM users WHERE username = %s;", 
                    [self.username]
                )

                for row in db.instance.fetchall():
                    self.passw = row[0]
                
                """ Verification stage
                """
                self.verify_login()
            else:
                self.error = 'The user you entered doesn\'t exist in our database.'
        except Exception as e:
            print(' 500 ERROR: ' + str(e))
            
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

