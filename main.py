from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)

db = SQLAlchemy(app)
import models

migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    return request.form['origin_url']

if __name__ == '__main__':
    app.run(debug=True)
