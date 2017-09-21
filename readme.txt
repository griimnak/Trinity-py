sudo apt-get install gunicorn3

nano app/Settings.py

pip3 install -r requirements.txt

sudo gunicorn3 -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 Core:app