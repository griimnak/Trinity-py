from app import app, Settings
from flask import render_template
import sys


@app.route('/index')
def landing():

    try:
        pyinfo = sys.version
    except:
        pyinfo = 'Unable to detect'

    return render_template('index.html',
        sitename=Settings.site['site_name'],
        sitedesc=Settings.site['site_desc'],
        siteport=Settings.server['server_port'],
        pyinfo=pyinfo
    )
