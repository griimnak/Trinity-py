import os

from flask import flash, redirect, request, session, url_for


def add_file_submit(formatted):
    try:
        open(formatted, 'a').close()

        flash(f'"{formatted}" successfully generated.', 'success')
    except Exception as e:
        flash(f'It seems "{formatted}" already exists. {str(e)}', 'error')


def delete_file_submit(path):
    try:
        os.remove(path)

        flash(f'"{path}" has been successfully deleted.', 'success')
    except Exception as e:
        flash(f'Unexpected error while deleting "{path}"; {str(e)}', 'error')


def add_file():
    if 'logged_in' and 'username' not in session:
        return redirect(url_for('admin_login'))
    else:
        if request.method == 'POST':
            if request.form['new-file-submit'] is not None:
                path = request.form['new-file-path']
                file = request.form['new-file']
                typeof = request.form['new-file-type']

                if path == '' or file == '' or typeof == '':
                    flash(u'A field has been left empty.', 'error')
                else:
                    formatted = f'{path}/{file}{typeof}'

                    add_file_submit(formatted)

                return redirect(url_for('admin_explorer'))
            else:
                return 'What did you do?'


def delete_file():
    if 'logged_in' and 'username' not in session:
        return redirect(url_for('admin_login'))
    else:
        if request.method == 'POST':
            if request.form['delete-file-submit'] is not None:
                path_to = request.form['delete-file']

                if path_to == '':
                    flash(u'A field has been left empty.', 'error')

                else:
                    delete_file_submit(path_to)

                return redirect(url_for('admin_explorer'))
            else:
                return 'What did you do?'
