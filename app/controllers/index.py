from app.config import Config
from flask import render_template
import sys


def controller():
    conf = Config()
    pyinfo = sys.version

    return render_template(
        'index.html',
        sitename=conf.read_key('site', 'name'),
        sitedesc=conf.read_key('site', 'desc'),
        siteport=conf.read_key('server', 'port'),
        mimetypes=conf.read_section('mimetypes'),
        pyinfo=pyinfo
    )
