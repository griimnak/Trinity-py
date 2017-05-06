from build import app
from build import settings
from flask import render_template
import sys


@app.route('/index')
def landing():

    try:
        pyinfo = sys.version
    except:
        pyinfo = 'Unable to detect'

    return render_template(
        '/index.html',
        sitename=settings.site['site_name'],
        sitedesc=settings.site['site_desc'],
        siteport=settings.server['server_port'],
        pyinfo=pyinfo
    )
