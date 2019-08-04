from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import datetime

import config


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)

db = SQLAlchemy(app)

class ShortUrl(db.Model):
    __tablename__ = 'short_url'

    key = db.Column('key', db.String(100), primary_key=True)
    url = db.Column('url', db.Text())
    created_at = db.Column('created_at', db.DateTime(), default=datetime.datetime.utcnow)
    count = db.Column('count', db.BigInteger(), default=1)

    def __init__(self, key, url, count):
        self.key = key
        self.url = url
        self.count = count

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    return request.form['origin_url']

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
