from app.config import Config
from os import listdir
from os.path import isfile, join
from flask import render_template, session, request, redirect, url_for

""" Controller for admin dashboard
"""
def controller():
    if session.get('logged_in') != True or session.get('username') is '':
        return redirect(url_for('admin_login'))
    else:
        from app.__admin.html_editor import HtmlEditor

        html = HtmlEditor().read('__admin__dash.html')

        path = 'app/views'
        tpls = [f for f in listdir(path) if isfile(join(path, f))]


        return render_template(
            '__admin__dash.html',
            username=session.get('username'),
            html=html,
            port=Config.read_key('server', 'port'),
            debug=Config.read_key('server', 'debug'),
            secret_key=Config.read_key('server', 'secret_key'),
            name=Config.read_key('site', 'name'),
            desc=Config.read_key('site', 'desc'),
            mhost=Config.read_key('mysqld', 'host'),
            muser=Config.read_key('mysqld', 'user'),
            mdb=Config.read_key('mysqld', 'db'),
            tpls=tpls
        )