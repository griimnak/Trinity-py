from flask import redirect, render_template, session, url_for


def view():
    """ Verify session """
    if 'logged_in' and 'username' not in session:
        return redirect(url_for('admin_login'))
    else:

        return render_template('admin/trinity_shell.html')
