from app.config import Config
from flask import render_template
import sys


def controller():
    cfg = Config()
    pyinfo = sys.version
  

    return render_template(
        'index.html',
        sitename=cfg.read_key('site', 'name'),
        sitedesc=cfg.read_key('site', 'desc'),
        siteport=cfg.read_key('server', 'port'),
        pyinfo=pyinfo

    )