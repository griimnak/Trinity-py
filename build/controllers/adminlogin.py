from build import app
from build import settings
from flask import render_template, session, url_for, redirect



@app.route('/admin/login', methods=['POST', 'GET'])
def admin_login():
	if session.get('logged_in') == True:
		return redirect(url_for('admin_dashboard'))
	else:
			
		from build.models.login import login
		logic = login()
		logic.loginSubmit()
			
		if session.get('logged_in') == True:
			return redirect(url_for('admin_dashboard'))

		return render_template('/admin-login.html', error=logic.error)
