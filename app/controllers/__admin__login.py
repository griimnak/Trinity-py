from app.config import Config
from flask import render_template, session, request

def controller():
    if session.get('logged_in') is True:
        return redirect(url_for('admin_dashboard'))
    else:
        if request.method == "POST":
            return "another day will come."


        return render_template('__admin__login.html')
