from urllib.parse import urlparse
import logging
from logging.config import dictConfig
from flask import Flask, render_template, request, redirect
import config
from functions import (
    gen_key,
    get_url_by_key,
    insert_record
)

dictConfig(config.LOGGING)

app = Flask(__name__)
app.config.from_object('config.Config')
logger = logging.getLogger('root')
r = config.REDIS

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

    key = gen_key(url)
    insert_record(r, key, url)
    short_url = "{}/{}".format(config.HOST, key)
    logger.info("Generate URL {} completed, save to DB".format(short_url))

    return short_url

@app.route('/<key>', methods=['GET'])
def redirect_to(key):
    url = get_url_by_key(r, key)
    logger.info("Receive redierct request with key {}, redirect to {}".format(key, url))
    return redirect(url)

if __name__ == '__main__':
    app.run()
