from flask import render_template, session
from flask import request, redirect, url_for, flash
from datetime import datetime
import sys
from app.config import Config
import urllib
from app import app


""" Lists routes for dash table """
conf = Config()
pyinfo = ".".join(map(str, sys.version_info[:3]))

def list_routes():
    output = []
    for rule in app.url_map.iter_rules():
        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)

        url = url_for(rule.endpoint, **options)
        __endpoint = urllib.parse.unquote("{}".format(rule.endpoint))
        __methods = urllib.parse.unquote("{}".format(methods))
        __url = urllib.parse.unquote("{}".format(url))

        stored = {}
        stored['endpoint'] = __endpoint
        stored['methods'] = __methods
        stored['url'] = __url

        output.append(stored)
    return output


""" Controller start """


def controller():
    """ Verify session """
    if 'logged_in' and 'username' not in session:
        return redirect(url_for('admin_login'))
    else:
        from app.modules.content_editor import ContentEditor

        error = None
        __content = None
        success = None

        try:
            """ Find requested content
            """
            __content = ContentEditor('config.json').read()

        except Exception as load_error:
            error = "Couldn't find what you requested.\n" + str(load_error)    

        """ Post trigger
        """
        if request.method == "POST":
            if request.form['update-submit'] != None:
                try:
                    """ Write content and flash success with timestamp
                        if trigger passes
                    """
                    __write = ContentEditor('config.json').write(
                        request.form['content']
                    )
                except Exception as write_error:
                    error = "Couldn't write content.\n" + str(write_error)

                date = datetime.now().strftime('%H:%M%p - %m-%d-%Y')
                flash(u"updated config.json (" + date + ")", 'success')
                return redirect(url_for('admin_dashboard'))

            else:
                return "What did you do?"


        return render_template(
            'admin/dash.html',
            html=__content,
            error=error,
            success=success,
            username=session.get('username'),
            urls=list_routes(),
            sitename=conf.read_key('site', 'name'),
            sitedesc=conf.read_key('site', 'desc'),
            siteport=conf.read_key('server', 'port'),
            pyinfo=pyinfo
        )
