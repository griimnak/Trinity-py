from build import app
from flask import render_template, session, url_for, redirect


@app.route('/admin/login', methods=['POST', 'GET'])
def admin_login():
    if session.get('logged_in') is True:
        return redirect(url_for('admin_dashboard'))
    else:
        # Import database model for admin login
        from build.models.adminlogin import Login

        if Login().verification is True:
            return redirect(url_for('admin_dashboard'))

        return render_template('/admin-login.html', error=Login().error)
