from flask import render_template, session, request, redirect, url_for

""" Controller for admin dashboard
"""
def controller():
    if session.get('logged_in') != True or session.get('username') is '':
        return redirect(url_for('admin_login'))
    else:
        from app.__admin.html_editor import HtmlEditor

        html = HtmlEditor().read('__admin__dash.html')

        return render_template(
            '__admin__dash.html',
            username=session.get('username'),
            html=html
        )