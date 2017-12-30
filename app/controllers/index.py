from app.config import Config
from flask import render_template
import sys

def splash():
    try:
        pyinfo = sys.version
    except:
        pyinfo = 'Unable to detect'

    return render_template(
        'index.html',
        sitename=Config.read_key('site', 'name'),
        sitedesc=Config.read_key('site', 'desc'),
        siteport=Config.read_key('server', 'port'),
        pyinfo=pyinfo

    )