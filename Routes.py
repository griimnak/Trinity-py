from app import app
from flask import redirect, url_for, session

# Define app root
@app.route('/')
def index():
    return redirect(url_for('landing'))


# Define admin handlers
@app.route('/admin/')
def admin():
    if session.get('logged_in') is True:
        return redirect(url_for('admin_dashboard'))
    else:
        return redirect(url_for('admin_login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('logged_in', None)

    return redirect(url_for('landing'))


# Define error handler
@app.errorhandler(404)
def page_not_found(error):
    return ' [NOTICE] ' + str(error)

@app.errorhandler(405)
def method_not_allowed(error):
    return ' [NOTICE] ' + str(error)

@app.errorhandler(500)
def syntax_error(error):
    return ' [NOTICE] ' + str(error)



