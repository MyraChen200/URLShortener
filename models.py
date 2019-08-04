import datetime
from main import db

class ShortUrl(db.Model):
    __tablename__ = 'short_url'

    key = db.Column('key', db.String(100), primary_key=True)
    url = db.Column('url', db.Text(), nullable=False)
    created_at = db.Column('created_at', db.DateTime(), default=datetime.datetime.utcnow)
    count = db.Column('count', db.BigInteger(), default=1)

    def __init__(self, key, url, count):
        self.key = key
        self.url = url
        self.count = count
