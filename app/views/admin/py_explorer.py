import os
# from datetime import datetime

from flask import flash, redirect, request, url_for
from flask import render_template, session


def list_files(path):
    try:
        files = [
            f for f in os.listdir(path)
            if os.path.isfile(os.path.join(path, f))
        ]
    except Exception as e:
        raise ValueError(
            'Trinity could not list files for: ' + path +
            ' Detailed error: ' + str(e)
        )

    return files


def view():
    """ Verify session """
    if 'logged_in' and 'username' not in session:
        return redirect(url_for('admin_login'))
    else:

        return render_template(
            'admin/py_explorer.html',
            username=session.get('username'),
            models=list_files('app/models'),
            modules=list_files('app/modules'),
            views=list_files('app/views'),
            tpls=list_files('app/templates'),
            auth=list_files('app/auth'),
            root=list_files('app')
        )


def edit_file(directory, file):
    if 'logged_in' and 'username' not in session:
        return redirect(url_for('admin_login'))
    else:
        content = None
        from app.modules.content_editor import ContentEditor
        try:
            if directory == 'app':
                replace = 'app'
                content = ContentEditor(replace+'/'+file).read()
            else:
                content = ContentEditor(
                    'app/' + directory + '/' + file
                ).read()
        except Exception as e:
            flash(u'Could not fulfil request  "' + directory + '/' +
                  file + '" was not found. ', 'error')

        if request.method == "POST":
            if request.form['update-submit'] is not None:
                # date = datetime.now().strftime('%H:%M%p - %m-%d-%Y')

                try:
                    if directory == 'app':
                        ContentEditor(directory + '/' + file).write(
                            request.form['content']
                        )
                        flash(
                            u'Changes successfully written to "' +
                            directory + '/' + file + '" ', 'success')
                    else:
                        ContentEditor(
                            'app/' + directory + '/'+file).write(
                            request.form['content']
                        )
                        flash(
                            u'Changes successfully written to "' +
                            'app/' + directory + '/'+file + '" ', 'success')

                    return redirect(
                        url_for('admin_py_explorer') +
                        '/' + directory + '/' + file
                    )
                except Exception as write_error:
                    flash(
                        u'Could not write changes ' +
                        str(write_error), 'error')

            else:
                return "What did you do?"

        return render_template(
            'admin/py_explorer.html',
            username=session.get('username'),
            models=list_files('app/models'),
            views=list_files('app/views'),
            tpls=list_files('app/templates'),
            modules=list_files('app/modules'),
            auth=list_files('app/auth'),
            root=list_files('app'),
            content=content,
            dir=directory,
            file=file
        )
