import configparser
from flask import render_template
import sys

def splash():
    config = configparser.ConfigParser()
    config.read('config.ini')

    try:
        pyinfo = sys.version
    except:
        pyinfo = 'Unable to detect'

    return render_template(
        'index.html',
        sitename=config['site']['name'],
        sitedesc=config['site']['desc'],
        siteport=config['server']['port'],
        pyinfo=pyinfo

    )
