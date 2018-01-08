from flask import render_template, session
from flask import request, redirect, url_for, flash
from datetime import datetime


def controller(content, file):
    """ Verify session
    """
    if 'logged_in' and 'username' not in session:
        return redirect(url_for('admin_dashboard'))
    else:
        from app.__trinity__.content_editor import ContentEditor

        error = None
        __content = None
        success = None

        try:
            """ Find requested content
            """
            __content = ContentEditor(content, file).read()

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
                    __write = ContentEditor(content, file).write(
                        request.form['content']
                    )
                except Exception as write_error:
                    error = "Couldn't write content.\n" + str(write_error)

                date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                flash("Updated: " + content + '/' + file + " (" + date + ")")
                return redirect(
                    url_for('admin_manage_home') +
                    '/' + 
                    content + 
                    '/' + 
                    file 
                )

            else:
                return "What did you do?"

        return render_template(
            '__admin__edit.html',
            html=__content,
            content=content,
            file=file,
            error=error,
            success=success,
            username=session.get('username'),
        )