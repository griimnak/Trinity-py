from flask import render_template, session, request, redirect, url_for

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
            from app.models.__admin__login import Login

            """ Redirect if verification passed
            """
            if Login().verification is True:
                return redirect(url_for('admin_dashboard'))

            error = Login().error

        return render_template('__admin__login.html', error=error)

