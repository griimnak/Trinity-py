from app import app, cached
from flask import redirect, url_for, session
from flask import render_template, make_response, request


@app.route('/')
@cached()
def landing():
    from app.controllers.index import splash
    return splash()


""" Error handlers
"""
@app.errorhandler(404)
def page_not_found(error):
    return ' [NOTICE] ' + str(error)

@app.errorhandler(405)
def method_not_allowed(error):
    return ' [NOTICE] ' + str(error)

@app.errorhandler(500)
def syntax_error(error):
    return ' [NOTICE] ' + str(error)

""" Application handlers
"""
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

""" Signature :p
"""
@app.after_request
def signature(response):
    response.headers['X-Powered-By'] = 'Trinity3-tr4'
    return response
