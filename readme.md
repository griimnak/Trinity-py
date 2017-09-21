Trinity 3.1
====
*WIP*

How to setup
-------------------
Install Python 3+
https://www.python.org/

Install MySQL Server
https://www.apachefriends.org/index.html

> Configure
app/Settings.py

--------------------
Run the command below to install required modules. (pip or pip3)

```sh
pip3 install -r requirements.txt
```

How to run
----------------
> Development / Local
```sh
python3 Core.py
```

> Production
```sh
gunicorn3 -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 Core:app
```

------------------

