from build import app
from build import settings
from flask import render_template, session, redirect, url_for

@app.route('/admin/dashboard/', methods=['POST', 'GET'])
def admin_dashboard():
	if session.get('logged_in') == True:
		return render_template('/admin-dashboard.html', username=session.get('username'))	
	else:
		return redirect(url_for('admin_login'))
			