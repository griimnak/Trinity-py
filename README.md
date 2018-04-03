<p align="center">
  <img src="https://i.imgur.com/RLmwuQK.png" alt="Trinity-py"/>
</p>

[![stability-experimental](https://img.shields.io/badge/stability-experimental-orange.svg)](https://github.com/emersion/stability-badges#experimental)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

*WIP* <br /> 

Recently rewritten for performance
-------------------
&#10004; gzip compression (flask-compress) <br />
&#10004; jinja2 caching <br />
&#10004; ujson ultra fast json <br />
###### Using least ammount of modules possible
flask, flask-compress, pymysql, passlib, ujson, argon2_cffi (encryption backend)

How to setup
-------------------
- Install Python 3+
https://www.python.org/

- Install MySQL Server
https://www.apachefriends.org/index.html

- Configure `config.json`
- Import `mysqldb.sql` into your database. (default user included tr4-admin:password)

--------------------
Run the command below to install required modules. (pip or pip3)

```sh
$ pip install -r requirements.txt
```

Q: How do i know what python verison pip is using?
```sh
$ pip -V
```

How to run
----------------
#### Local / development environment
```sh
python3 local_server.py
```
###### Windows users can simply launch `win_launch.bat`
--------------------

#### Gunicorn production environment
###### *Recommended way* (docs: <a href="http://docs.gunicorn.org/en/stable/run.html">gunicorn docs</a> <a href="https://djangodeployment.com/2016/11/30/how-to-setup-apache-with-gunicorn/">apache/nginx+gunicorn docs</a>)
```sh
$ gunicorn --workers=4 app:app
```
#### Passenger production environment
- See `passenger_wsgi.py`
###### (http://griimnak.me/trinity runs on passenger through cpanel)
----------------

<br /><br />


## Screenshots
[4/4/2018]
![Alt Text](https://image.prntscr.com/image/4H2mSa3fRjuOc_1Tc1xCOQ.png)

[4/2/2018]
![Alt Text](https://image.prntscr.com/image/Zz-AOXKQQHy8PcqfH2EAzQ.png)
