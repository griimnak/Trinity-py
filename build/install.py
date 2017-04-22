from passlib.hash import sha256_crypt as hasher
import datetime
# install check

def install_settings():
	print(' * MySQL Settings --')
	db_host = input(" * MySQL hostname (usually localhost): ")
	db_user = input(" * MySQL username: ")
	db_pass = input(" * MySQL password: ")
	db_name = input(" * MySQL database (cannot exist already): ")
	print(' * Site Settings --')
	site_name = input(" * Site name: ")
	site_desc = input(" * Site description: ")
	print(' * Server Settings --')
	server_skey = input(" * Server secret key (should be random and saved somewhere): ")
	server_host = input(" * Server hostname (usally localhost): ")
	server_port = input(" * Server port (should be 80, or enter a custom port): ")
	server_debug = input(" * Server debug mode (True or False): ")

	print(' * Attempting to write 18 lines into build/settings.py..')
	try:
		f = open('build/settings.py', 'a')
		f.write("")
		f.write("mysql = dict(\n")
		f.write("	db_host = '"+str(db_host)+"',\n")
		f.write("	db_user = '"+str(db_user)+"',\n")
		f.write("	db_pass = '"+str(db_pass)+"',\n")
		f.write("	db_name = '"+str(db_name)+"'\n")
		f.write("	)\n\n")
		f.write("site = dict(\n")
		f.write('	site_name = "'+str(site_name)+'",\n')
		f.write('	site_desc = "'+str(site_desc)+'",\n')
		f.write("	)\n\n")
		f.write("server = dict(\n")
		f.write("	server_skey = '"+str(server_skey)+"',\n")
		f.write("	server_host = '"+str(server_host)+"',\n")
		f.write("	server_port = "+str(server_port)+",\n")
		f.write("	server_debug = "+str(server_debug)+"\n")
		f.write("	)\n\n")
	except Exception as e:
		print(' [NOTICE] Failed writing configuration file! '+str(e))
	
	print(' * Configuration set! Attempting to create database "'+db_name+'"..')
	try:
		import pymysql

		conn = pymysql.connect(user=str(db_user), passwd=str(db_pass))
		conn.autocommit(True)
		conn.cursor().execute("CREATE DATABASE "+db_name+";")
	except Exception as error:
		print(' [NOTICE] Failed creating databse! '+str(error))

	print(' * Setup complete! Please re-launch trinity.')
	exit()

def install_database():
	from build import database
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