from build import app
from build import settings
from flask import render_template, session, redirect, url_for
import sys
import os


@app.route('/admin/home/dashboard/', methods=['POST', 'GET'])
def admin_dashboard():
    if session.get('logged_in') is True:
        try:
            pyinfo = sys.version
        except:
            pyinfo = 'Unable to detect'

        templates = 0
        try:
            for f in os.listdir('build/views/'):
                templates += 1
        except:
            templates = '?'

        return render_template(
            '/admin-dashboard.html',
            username=session.get('username'),
            site_name=settings.site['site_name'],
            site_desc=settings.site['site_desc'],
            site_tpl=settings.site['site_tpl'],
            server_host=settings.server['server_host'],
            server_port=settings.server['server_port'],
            server_debug=settings.server['server_debug'],
            db_user=settings.mysql['db_user'],
            db_name=settings.mysql['db_name'],
            tpls=templates,
            pyinfo=pyinfo
            )
    else:
        return redirect(url_for('admin_login'))


@app.route('/admin/home/')
def redirect_home():
    return redirect(url_for('admin_dashboard'))
