<p align="center">
  <img src="http://i.imgur.com/k8I15Gh.png" alt="Trinity 3"/>
</p>

[![stability-experimental](https://img.shields.io/badge/stability-experimental-orange.svg)](https://github.com/emersion/stability-badges#experimental)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

*WIP* <br /> live demo: http://griimnak.me/trinity

Recently rewritten for performance
-------------------
&#10004; gzip compression (flask-compress) <br />
&#10004; Jinja2 caching <br />
###### Using least ammount of modules possible
flask, flask-compress, pymysql, passlib

How to setup
-------------------
- Install Python 3+
https://www.python.org/

- Install MySQL Server
https://www.apachefriends.org/index.html

- Configure `config.ini`

--------------------
Run the command below to install required modules. (pip or pip3)

```sh
pip3 install -r requirements.txt
```

How to run
----------------
#### Local / development environment
```sh
python3 trinity_server.py
```
###### Windows users can simply launch `win_launch.bat`
--------------------

#### Gunicorn production environment
###### *Recommended way* (docs: <a href="http://docs.gunicorn.org/en/stable/run.html">gunicorn docs</a> <a href="https://djangodeployment.com/2016/11/30/how-to-setup-apache-with-gunicorn/">apache/nginx+gunicorn docs</a>)
```sh
gunicorn --workers=4 app:app
```
#### Passenger production environment
- See `passenger_wsgi.py`
###### (http://griimnak.me/trinity runs on passenger through cpanel)
----------------

<br /><br />


## Screenshots
![Alt Text](https://i.imgur.com/80209wU.png)
![Alt Text](https://image.prntscr.com/image/-MN-_eHZQNKlkJVUqPC0rQ.png)
