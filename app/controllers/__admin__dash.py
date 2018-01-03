from app.config import Config
from os import listdir
from os.path import isfile, join
from flask import render_template, session, request, redirect, url_for

""" Controller for admin dashboard
"""
def controller():
    if 'logged_in' and 'username' not in session:
        return redirect(url_for('admin_login'))
    else:

        """ This will all be tidy'd up eventually, just for testing,
        """

        path = 'app/views'
        tpls = [f for f in listdir(path) if isfile(join(path, f))]

        count = len(
            [name for name in listdir(path) if isfile(join(path, name))]
        )

        pathm = 'app/models'
        countm = len(
            [name for name in listdir(pathm) if isfile(join(pathm, name))]
        )
        
        pathc = 'app/controllers'
        countc = len(
            [name for name in listdir(pathc) if isfile(join(pathc, name))]
        )

        return render_template(
            '__admin__dash.html',
            username=session.get('username'),
            port=Config.read_key('server', 'port'),
            debug=Config.read_key('server', 'debug'),
            secret_key=Config.read_key('server', 'secret_key'),
            name=Config.read_key('site', 'name'),
            desc=Config.read_key('site', 'desc'),
            mhost=Config.read_key('mysqld', 'host'),
            muser=Config.read_key('mysqld', 'user'),
            mdb=Config.read_key('mysqld', 'db'),
            tpls=tpls,
            count=count,
            countc=countc,
            countm=countm
        )