import hashlib
from urllib.parse import urlparse
import logging
from logging.config import dictConfig
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

dictConfig(config.LOGGING)

app = Flask(__name__)
app.config.from_object('config.Config')
logger = logging.getLogger('root')

db = SQLAlchemy(app)
import models
from models import *
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    url = request.form['origin_url']
    logger.info("Start to convert url: {}".format(url))

    if not urlparse(url).scheme:
        logger.info("Got not validate URL: {}, skip it".format(url))
        return "Please enter a validate URL", 400

    exist_key = get_exist_url(url)
    if exist_key:
        short_url = "{}/{}".format(config.HOST, exist_key)
        logger.info("URL {} be generated already, return exist short URL: {}".format(url, short_url))
        return short_url

    key = gen_key(url)
    insert_record(key, url)
    short_url = "{}/{}".format(config.HOST, key)
    logger.info("Generate URL {} completed, save to DB".format(short_url))

    return short_url

@app.route('/<key>', methods=['GET'])
def redirect_to(key):
    url = get_url_by_key(key)
    logger.info("Receive redierct request with key {}, redirect to {}".format(key, url))
    return redirect(url)

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
    app.run()
