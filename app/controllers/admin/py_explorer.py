from flask import render_template, session
from flask import redirect, url_for


def controller():
    """ Verify session
    """
    if 'logged_in' and 'username' not in session:
        return redirect(url_for('admin_login'))
    else:

        return render_template(
            'admin/py_explorer.html',
            username=session.get('username')
        )
