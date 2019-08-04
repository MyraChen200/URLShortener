import hashlib
from urllib.parse import urlparse
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)

db = SQLAlchemy(app)
import models
from models import *
migrate = Migrate(app, db)

HOST = "http://localhost:5000"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    url = request.form['origin_url']
    if not urlparse(url).scheme:
        return "Please enter a validate URL", 400

    exist_key = get_exist_url(url)
    if exist_key:
        return "{}/{}".format(HOST, exist_key)

    key = gen_key(url)
    insert_record(key, url)
    return "{}/{}".format(HOST, key)

@app.route('/<key>', methods=['GET'])
def redirect_to(key):
    return redirect(get_url_by_key(key))

def gen_key(url):
    return hashlib.md5(url.encode("utf-8")).hexdigest()[:10]

def get_exist_url(url):
    record = ShortUrl.query.filter_by(url=url).first()
    if record:
        record.count += 1
        db.session.commit()
        return record.key
    return None

def get_url_by_key(key):
    return ShortUrl.query.filter_by(key=key).first().url

def insert_record(key, url):
    record = ShortUrl(key=key, url=url, count=1)
    db.session.add(record)
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
