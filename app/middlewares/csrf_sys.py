import os
import binascii
from app import app
from flask import request, session, abort

""" Simple but effective csrf token generator
    binascii.hexlify(os.urandom()) is apparently faster than uuid
    /shrug
"""

def generate_random_string(n):
    result = binascii.hexlify(os.urandom(n))

    return(result.decode('UTF-8'))

def generate_csrf_token():
    return generate_random_string(12)

app.jinja_env.globals['csrf_token'] = generate_csrf_token  