from app import app
from flask import redirect, url_for, session, render_template

""" Error handlers
"""
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error=error)
@app.errorhandler(405)
def method_not_allowed(error):
    return render_template('404.html', error=error)
@app.errorhandler(500)
def syntax_error(error):
    return render_template('404.html', error=error)

""" Application handlers
"""
@app.route('/admin/')
def admin():
    if 'logged_in' and 'username' in session:
        return redirect(url_for('admin_dashboard'))
    else:
        return redirect(url_for('admin_login'))

@app.route('/admin/manage/<content>/<file>', methods=['POST', 'GET'])
def admin_manage(content, file):
    from app.controllers.__admin__edit import controller
    return controller(content, file)
    

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('logged_in', None)

    return redirect(url_for('landing'))

""" Signature :p
"""
@app.after_request
def signature(response):
    response.headers['X-Powered-By'] = 'Trinity3-tr4.2'
    return response