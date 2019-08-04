# URLShortener
Written in Python 3.7, apache 2.4
Support env: osx, linux

## Before deploy
Confirm DB config and related path correct
Make virtual env and into it
```
virtualenv pyvenv
source pyvenv/bin/activate
```

Install required packages
```
pip install -r requirement.txt
```

Migrate DB
```
export FLASK_APP=main.py
flask db upgrade
```

## Deploy steps:
copy project to /var/www/
modify /var/www/URLShortener/app.log permission for write log
copy URLShortener/installation/flask.conf to /etc/apache2/other/
restart apache

Website will show on http://127.0.0.1 (http://0.0.0.0)
