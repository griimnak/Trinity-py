from flask import render_template, session, request, redirect, url_for
from app.models.__admin__login import Login
""" Controller for admin login page
"""
def controller():
    if 'logged_in' and 'username' in session:
        return redirect(url_for('admin_dashboard'))
    else:
        error = None
        """ Post trigger
        """
        if request.method == "POST":
            if request.form['login-submit'] != None:
                submit = None

                username = request.form['username']
                password = request.form['password']

                """ Check if fields are blank
                """
                if username == '' or password == '':
                    error = 'One or more fields have been left blank.'

                else:
                    """ Login
                    """
                    submit = Login(username, password)

                    if submit.verification is True:
                        
                        return redirect(url_for('admin_dashboard'))

                    error = submit.error          
            else:
                error =  "What did you do?"
            """ Redirect if verification passed
            """
           

        return render_template('__admin__login.html', error=error)

