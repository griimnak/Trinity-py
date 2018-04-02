from app import app
from flask import redirect, url_for, session, render_template

""" Application routes """


@app.route('/')
def index():
    from app.controllers.index import controller
    return controller()


@app.route('/admin/login', methods=['POST', 'GET'])
def admin_login():
    from app.controllers.admin.login import controller
    return controller()


@app.route('/admin/dashboard', methods=['POST', 'GET'])
def admin_dashboard():
    from app.controllers.admin.dash import controller
    return controller()


""" Error handlers """


@app.errorhandler(404)
def page_not_found(error): return render_template('404.html', error=error)


@app.errorhandler(405)
def method_not_allowed(error): return render_template('404.html', error=error)


@app.errorhandler(500)
def syntax_error(error): return render_template('404.html', error=error)


@app.route('/admin/')
def admin():
    if 'logged_in' and 'username' in session:
        return redirect(url_for('admin_dashboard'))
    else:
        return redirect(url_for('admin_login'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('logged_in', None)

    return redirect(url_for('index'))


@app.after_request
def signature(response):
    response.headers['X-Powered-By'] = 'Trinity3-tr4.2'
    return response

