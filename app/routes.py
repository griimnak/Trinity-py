from app import app
from flask import redirect, url_for, session, render_template

""" Public routes 
    <public routes>
"""


@app.route('/')
def index(): from app.views.index import view; return view()


""" </public routes>
"""

@app.route('/admin/login')
def admin_login(): from app.views.admin.login import view; return view()


@app.route('/admin/dashboard', methods=['POST', 'GET'])
def admin_dashboard(): from app.views.admin.dash import view; return view()


@app.route('/admin/py_explorer', methods=['POST', 'GET'])
def admin_py_explorer(): from app.views.admin.py_explorer import view; return view()


@app.route('/admin/py_explorer/<dir>/<file>', methods=['POST', 'GET'])
def admin_py_explorer_edit(dir, file): from app.views.admin.py_explorer import edit_file; return edit_file(dir, file)

@app.errorhandler(404)
def page_not_found(error): return render_template('admin/error.html', error=error)


@app.errorhandler(405)
def method_not_allowed(error): return render_template('admin/error.html', error=error)


@app.errorhandler(500)
def syntax_error(error): return render_template('admin/error.html', error=error)


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


@app.route('/admin/login/submit', methods=['POST'])
def admin_login_submit():
    from app.auth.login_submit import login_submit

    return login_submit()


