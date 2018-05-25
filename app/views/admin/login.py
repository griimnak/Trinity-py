from flask import redirect, render_template, request, session, url_for


def view():
    origin = request.environ.get('HTTP_X_REAL_IP', request.remote_addr) or \
        '[unknown ip_addr]'

    user_agent = request.headers.get('User-Agent') or \
        '[unknown user_agent]'

    if 'logged_in' and 'username' in session:
        return redirect(url_for('admin_dashboard'))

    return render_template(
        'admin/login.html', origin=origin, user_agent=user_agent
    )
