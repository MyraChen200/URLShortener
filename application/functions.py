import hashlib

def gen_key(url):
    return hashlib.md5(url.encode("utf-8")).hexdigest()[:10]


def get_url_by_key(r, key):
    return r.get(key)


def insert_record(r, key, url):
    pipe = r.pipeline()
    pipe.set(key, url)
    pipe.incr(f"{url}:hit")
    pipe.execute()
