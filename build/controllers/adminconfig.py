from build import app
from build import settings
from flask import render_template, session, redirect, url_for


@app.route('/admin/home/configuration/', methods=['POST', 'GET'])
def admin_configuration():
    if session.get('logged_in') is True:

        return render_template(
            '/admin-configuration.html',
            username=session.get('username'),
            site_name=settings.site['site_name'],
            site_desc=settings.site['site_desc'],
            site_tpl=settings.site['site_tpl'],
            server_host=settings.server['server_host'],
            server_port=settings.server['server_port'],
            server_debug=settings.server['server_debug'],
            db_user=settings.mysql['db_user'],
            db_name=settings.mysql['db_name']
            )
    else:
        return redirect(url_for('admin_login'))