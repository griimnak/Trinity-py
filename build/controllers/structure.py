from build import app
from build import settings
from flask import render_template, redirect, url_for, session


# Define App root
@app.route('/')
def index():
	return redirect(url_for('landing'))

# Admin handler
@app.route('/admin/')
def admin():
	if session.get('logged_in') == True:
		return redirect(url_for('admin_dashboard'))
	else:
		return redirect(url_for('admin_login'))

@app.route('/logout')
def logout():
	session.pop('username', None)
	session.pop('logged_in', None)

	return redirect(url_for('landing'))

# Define Error Handlers	
@app.errorhandler(404)
def page_not_found(error):
	return 'page not found, man.'

@app.errorhandler(405)
def method_not_allowed(error):
	return 'POST/GET not allowed on this page, man.'

@app.errorhandler(500)
def syntax_error(error):
	return 'Something\'s wrong with the code, man.'

	


