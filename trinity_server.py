#!/usr/bin/env python
from engine import app
from gevent.wsgi import WSGIServer
from build import settings

#---------------------------------------------\
# Begins WSGI on given port in 
# build/settings, using gevent.
#---------------------------------------------/
print (' * Starting WSGI server on port', settings.server['server_port'],'..')
try:
	http_server = WSGIServer(('', settings.server['server_port']), app)
	http_server.serve_forever()
except:
	print (' * Failed to start WSGI Server! Port:', settings.server['server_port'], 'may be in use.')

