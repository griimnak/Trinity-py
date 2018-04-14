from app import app

from flask import redirect, request, render_template, session, url_for

""" Public routes
    <public routes>
"""


@app.route('/')
def index():
    from app.views.index import view
    return view()


""" </public routes>
"""


@app.route('/admin/login')
def admin_login():
    from app.views.admin.login import view
    return view()


@app.route('/admin/dashboard', methods=['POST', 'GET'])
def admin_dashboard():
    from app.views.admin.dash import view
    return view()


@app.route('/admin/explorer', methods=['POST', 'GET'])
def admin_explorer():
    from app.views.admin.explorer import view
    return view()


@app.route('/admin/explorer/<dir>/<file>', methods=['POST', 'GET'])
def admin_explorer_edit(dir, file):
    from app.views.admin.explorer import edit_file
    return edit_file(dir, file)


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
    from app.posts.admin.login_submit import login_submit
    return login_submit()


@app.route('/admin/explorer/addfile', methods=['POST'])
def admin_newfile_submit():
    from app.posts.admin.file_add_remove import add_file
    return add_file()


@app.route('/admin/explorer/deletefile', methods=['POST'])
def admin_deletefile_submit():
    from app.posts.admin.file_add_remove import delete_file
    return delete_file()


@app.route('/admin/shell')
def admin_trinity_shell():
    from app.views.admin.trinity_shell import view
    return view()


@app.route('/admin/shell/submit')
def admin_trinity_shell_submit():
    if 'logged_in' and 'username' not in session:
        return redirect(url_for('admin_login'))
    else:
        from app.modules.trinity_shell import TrinityShell
        shell_request = TrinityShell(request.args.get('shellinput'))
        return shell_request.response


@app.errorhandler(404)
def page_not_found(error):
    return render_template('admin/error.html', error=error)


@app.errorhandler(405)
def method_not_allowed(error):
    return render_template('admin/error.html', error=error)


@app.errorhandler(500)
def syntax_error(error):
    return render_template('admin/error.html', error=error)
