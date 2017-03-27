# -*- coding: utf-8 -*-

mysql = dict(
	#---------------------------------------------\
	# -- Configuration for MySQLdb
	# -- db_host: Hostname
	# -- db_user: Mysql username
	# -- db_pass: Mysql password
	# -- db_name: Mysql database
	#---------------------------------------------/
	db_host = 'localhost',
	db_user = '',
	db_pass = '',
	db_name = ''
	)

site = dict(
	#---------------------------------------------\
	# -- Configuration for the site
	# -- site_name: Site's name (displayed in titles etc)
	# -- site_desc: Site's description
	#---------------------------------------------/
	site_name = 'Trinity 3',
	site_desc = 'A python cms, written by griimnak.'
	)

server = dict(
	#---------------------------------------------\
	# -- Configuration for Trinity's webserver
	# -- server_skey: Secret server key. 
	# -- server_host: Usualy localhost
	# -- server_port: Usualy 80, unless you want this panel to be on a dedicated port. (or reverse proxy?)
	#---------------------------------------------/
	server_skey = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT',
	server_host = 'localhost',
	server_port = 80,
	server_debug = True
	)