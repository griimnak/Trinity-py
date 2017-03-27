from build import database
from passlib.hash import sha256_crypt as hasher
import datetime
# install check


def checkInstall():
	try:
		#--
		# Run a dummy query, if it returns true the tables exist.
		#--
		query = 'SELECT ip_addr FROM trinity_logs'
		database.instance.execute(query)
		print (' * Required tables loaded successfully..')

	except Exception as e:

		check = input(" [NOTICE] Required tables not found. Would you like to run the installer? y/n ")

		if check == 'n':
			print (' [NOTICE] Continuing without required tables!')
		elif check == 'y':
			print (' * Running installer..\n * Created: trinity_logs\n * Created: trinity_messages\n * Created: trinity_blacklist\n * Created: trinity_users\n * Created: trinity_views_log')
			try:
				#--
				# Execute Trinity table creation if user-input: y
				#--
				sql = '''
						CREATE TABLE IF NOT EXISTS trinity_logs (
							ip_addr varchar(255) NOT NULL,
							browser varchar(255) NOT NULL,
							type varchar(255) NOT NULL,
							time varchar(255) NOT NULL
						) ENGINE=InnoDB DEFAULT CHARSET=latin1;

						CREATE TABLE IF NOT EXISTS trinity_posts (
							title varchar(255) NOT NULL,
							content varchar(255) NOT NULL,
							link varchar(255) NOT NULL,
							location varchar(255) NOT NULL
						) ENGINE=InnoDB DEFAULT CHARSET=latin1;

						CREATE TABLE IF NOT EXISTS trinity_blacklist (
							ip_addr varchar(255) NOT NULL,
							reason varchar(255) NOT NULL,
							date varchar(255) NOT NULL
						) ENGINE=InnoDB DEFAULT CHARSET=latin1;

						CREATE TABLE IF NOT EXISTS trinity_users (
							username varchar(255) NOT NULL,
							password varchar(255) NOT NULL,
							last_login varchar(255) NOT NULL,
							last_ip varchar(255) NOT NULL
						) ENGINE=InnoDB DEFAULT CHARSET=latin1;


						CREATE TABLE IF NOT EXISTS trinity_views_log (
							ip varchar(255) NOT NULL
						) ENGINE=InnoDB DEFAULT CHARSET=latin1;
						'''
				database.instance.execute(sql)
			except Exception as e:
				#--
				# When some funky shit happens..
				#--
				print (' [ERROR] Unable to create required tables.')

			createSuperUser = input(" [NOTICE] User table empty, let's create a super user now? y/n")

			if createSuperUser == 'n':
				print (' [NOTICE] Not creating an admin account, setup is -> DONE!')
			elif createSuperUser == 'y':
				username = input(" >> Please enter a desired username: ")

				if username == '':
					username = input(" >> Please enter a desired username: ")

				password = input(" >> Please enter a secure password: ")

				if password == '':
					password = input(" >> Please enter a secure password: ")

				hashedPassword = hasher.encrypt(password)
				print (' * Running query ..')

				sql = 'INSERT INTO trinity_users (username, password, last_ip, last_login) VALUES (%s, %s, %s, %s);'
				time = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
				if database.instance.execute(sql, [username, hashedPassword, '127.0.0.1', time]):
					print (' * Super user:', username, ' created, setup is -> DONE!')
				else:
					print (' [ERROR] Unable to create super user!')