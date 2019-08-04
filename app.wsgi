activate_this = '/var/www/URLShortener/pyvenv/bin/activate_this.py'

with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys, os
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/URLShortener")
from main import app as application
application.secret_key = 'x!jiccf+x5&253qnci-hcosp*=1=+soo2($8-f!^oi%w(0(rs!'
