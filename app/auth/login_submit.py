from flask import flash, session, request, redirect, url_for
from app.models.admin.login import Login
from datetime import datetime
from pymysql import escape_string as clean

def login_submit():
    """ Post trigger """
    if request.method == 'POST':
        if request.form['login-submit'] == 'Login':
            username = clean(request.form['username'])
            password = clean(request.form['password'])

            """ Check if fields are blank """
            if username == '' or password == '':
                flash(u'One or more fields have been left blank.', 'error')
            else:

                """ Login """
                submit = Login(username, password)

                if submit.verification is True:
                    printed = '. Session started at ' + datetime.now().strftime('%H:%M%p - %m-%d-%Y')
                    flash(u'Welcome back, ' + username + printed, 'login-welcome')

                    session['username'] = username
                    session['logged_in'] = True
                else:

                    flash(submit.error, 'error')
        else:
            flash(u'What did you do?', 'error')

    return redirect(url_for('admin_login'))