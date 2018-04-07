from datetime import datetime

from app.models.admin.login import Login

from flask import flash, redirect, request, session, url_for

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
                timestamp = datetime.now().strftime('%H:%M%p - %m-%d-%Y')

                if submit.verification is True:
                    printed = 'Session started at {}'.format(timestamp)
                    flash(u'Welcome back, {}. {}'.format(username, printed),
                          'login-welcome')

                    session['username'] = username
                    session['logged_in'] = True
                else:

                    flash(submit.error, 'error')
        else:
            flash(u'What did you do?', 'error')

    return redirect(url_for('admin_login'))
