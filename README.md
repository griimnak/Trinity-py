<p align="center">
  <img src="https://i.imgur.com/RLmwuQK.png" alt="Trinity-py"/>
</p>

[![stability-experimental](https://img.shields.io/badge/stability-stable-green.svg)](https://github.com/emersion/stability-badges#stable)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

*WIP* [Youtube Demonstration](https://youtu.be/4mDjhz5wBPU)<br />

This is a flask build of Trinity-py. <a href="https://github.com/griimnak/Trinity-py/tree/tr4.5">Pure WSGI branch</a> is in development and the future of Trinity-py.

Recently rewritten for performance
-------------------
&#10004; gzip compression (flask-compress) <br />
&#10004; jinja2 caching <br />
&#10004; py3.6+ f-strings <a href="https://cito.github.io/img/f-strings-1.png">bench</a> <br />
&#10004; mysql high concurrency <a href="https://docs.google.com/spreadsheets/d/e/2PACX-1vTgKrdlePZ0VoWyrpZI8MuzDOf-PR5Vsa2VPoXb3dCQxEVt3d3y-4-6oHNSyQxMraGgSVf1HZQHsk0m/pubchart?oid=75267628&amp;format=image">bench</a> <br />
&#10004; ujson ultra fast json <a href="https://artem.krylysov.com/images/2015-benchmark-python-json/benchmark-json-python3.png">bench</a> <br />
###### Using least ammount of modules possible
flask, flask-compress, pymysql, passlib, ujson, argon2_cffi (encryption backend)

How to setup
-------------------
- Install Python 3.6+
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
<b>Trinity was built with compatibility in mind for multiple setups.</b> 

#### Local / development environment
```sh
$ python local_server.py
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

#### Windows waitress production environment
###### *Waitress is a gunicorn alternative for windows.* 
```sh
$ pip install waitress
$ waitress-serve --listen=127.0.0.1:80 -w 4 app:app
```
----------------

<br /><br />


## Screenshots
[4/10/2018]
![Alt Text](https://image.prntscr.com/image/AQunvVnpRe6AJFNyJNrnSg.png)

[4/5/2018]
![Alt Text](https://image.prntscr.com/image/UJOl5v_7T2ywvwOkq8ahKg.png)

[4/4/2018]
![Alt Text](https://image.prntscr.com/image/4H2mSa3fRjuOc_1Tc1xCOQ.png)

[4/2/2018]
![Alt Text](https://image.prntscr.com/image/Zz-AOXKQQHy8PcqfH2EAzQ.png)
