from flask import Flask, request, url_for, redirect, session, flash
from passlib.hash import sha256_crypt as hasher
from build import database
from pymysql import escape_string as clean

class login(object):

	def __init__(self):
		self.error = None

	def loginSubmit(self):

		if request.method == 'POST':
			username = request.form['username']
			password = request.form['password']

			if username == '' or password == '':
				self.error = 'One or more fields have been left blank.'
			else:
				try:
					database.instance.execute("SELECT COUNT(1) FROM trinity_users WHERE username = %s;", [clean(username)])

					if database.instance.fetchone()[0]:
						database.instance.execute("SELECT password FROM trinity_users WHERE username = %s;", [clean(username)])

						for row in database.instance.fetchall():
							passw = row[0]

						verify = hasher.verify(clean(password), clean(passw))
						if verify == True:
							# start sessions
							session['username'] = clean(username)
							session['logged_in'] = True
						else:
							self.error = 'Incorrect password for ' + clean(username)
					else:
						self.error = 'The user you entered doesn\'t exist in the database.'
				except Exception as e:
					return redirect(url_for('syntax_error'))

