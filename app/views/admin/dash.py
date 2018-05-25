from datetime import datetime
from sys import version_info
from urllib import parse

from app import app
from app import conf

from flask import flash, redirect, request, url_for
from flask import render_template, session
pyinfo = ".".join(map(str, version_info[:3]))


def list_routes():
    output = []
    for rule in app.url_map.iter_rules():
        route = {}
        options = {}

        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)

        url = url_for(rule.endpoint, **options)

        __endpoint = parse.unquote("{}".format(rule.endpoint))
        __methods = parse.unquote("{}".format(methods))
        __url = parse.unquote("{}".format(url))

        route['endpoint'] = __endpoint
        route['methods'] = __methods
        route['url'] = __url

        output.append(route)
    return output


def view():
    """ Verify session """
    if 'logged_in' and 'username' not in session:
        return redirect(url_for('admin_login'))
    else:
        from app.modules.content_editor import ContentEditor
        error = None
        success = None
        config = None

        """ Load configuration """
        try:
            config = ContentEditor('config.json').read()
        except Exception as load_error:
            error = "Couldn't find what you requested.\n" + str(load_error)

        """ Update config trigger """

        if request.method == "POST":
            if request.form['update-submit'] is not None:

                try:
                    ContentEditor('config.json').write(request.form['content'])

                    date = datetime.now().strftime('%H:%M%p - %m-%d-%Y')
                    flash(u"updated config.json (" + date + ")", 'success')
                except Exception as write_error:
                    error = "Couldn't write content.\n" + str(write_error)

                return redirect(url_for('admin_dashboard'))
            else:
                return "What did you do?"

        return render_template(
            'admin/dash.html',
            config=config,
            error=error,
            success=success,
            username=session.get('username'),
            urls=list_routes(),
            sitename=conf.read_key('site', 'name'),
            sitedesc=conf.read_key('site', 'desc'),
            siteport=conf.read_key('server', 'port'),
            pyinfo=pyinfo
        )
