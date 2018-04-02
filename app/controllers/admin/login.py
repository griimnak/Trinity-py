from flask import render_template, session, request, redirect, url_for
from app.auth.admin_auth import Login
from pymysql import escape_string as clean
""" Controller for admin login page """


def controller():
    if 'logged_in' and 'username' in session:
        return redirect(url_for('admin_dashboard'))
    else:
        """ Post trigger """
        error = None
        if request.method == "POST":
            if request.form['login-submit'] is not None:
                submit = None
                username = clean(request.form['username'])
                password = clean(request.form['password'])

                """ Check if fields are blank """
                if username == '' or password == '':
                    error = 'One or more fields have been left blank.'

                else:
                    """ Login """
                    submit = Login(username, password)

                    if submit.verification is True:
                        return redirect(url_for('admin_dashboard'))

                    error = submit.error
            else:
                error = "What did you do?"

        """ Redirect if verification passed """
        origin = request.environ.get('HTTP_X_REAL_IP', request.remote_addr) or '[unknown ip_addr]'
        user_agent = request.headers.get('User-Agent') or '[unknown user_agent]'
        return render_template('admin/login.html', error=error, origin=origin, user_agent=user_agent)
