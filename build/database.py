import pymysql
from build import settings
#---------------------------------------------\
# Create a database instance
#---------------------------------------------/

conn = pymysql.connect(
	settings.mysql['db_host'], 
	settings.mysql['db_user'], 
	settings.mysql['db_pass'], 
	settings.mysql['db_name']
	)

def validate_connection():
	if conn.open == 0:
		print(' * Database connection failed.')
	else:
		print(' * Database connected successfully!')

conn.autocommit(True)
instance = conn.cursor()