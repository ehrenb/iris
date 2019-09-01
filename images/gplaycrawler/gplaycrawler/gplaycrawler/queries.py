import functools
import time

import psycopg2 

from settings import db_config

def retry(tries=3):
    def deco_retry(f):
        @functools.wraps(f)
        def wrapper (*args, **kwargs):
            tries = 0
            max_tries = 5
            while tries < max_tries:
                try:
                    return f(*args, **kwargs)
                except psycopg2.DatabaseError:
                    tries+=1
                    if tries==max_tries:
                        raise
                    time.sleep(1)
                    
        return wrapper
    return deco_retry


@retry(tries=5)
def get_conn():
    conn = psycopg2.connect(**db_config)
    return conn

@retry()
def get_cursor(conn):
    cur = conn.cursor()
    return cur

@retry()
def insert_app(cursor, item):
    cursor.execute("""insert into apps 
                    (app_id, item_name, updated, author, filesize, downloads, version, version_code, compatibility, content_rating, author_link, genre, price, rating_value, review_number, description, iap, developer_badge, physical_address, video_url, developer_id) 
                    values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", (item["Package"],
                                                                                                                      item["Item_name"],
                                                                                                                      item["Updated"],
                                                                                                                      item["Author"],
                                                                                                                      item["Filesize"],
                                                                                                                      item["Downloads"],
                                                                                                                      item["Version"],
                                                                                                                      item['version_code'],
                                                                                                                      item["Compatibility"],
                                                                                                                      item["Content_rating"],
                                                                                                                      item["Author_link"],
                                                                                                                      item["Genre"],
                                                                                                                      item["Price"],
                                                                                                                      item["Rating_value"],
                                                                                                                      item["Review_number"],
                                                                                                                      item["Description"],
                                                                                                                      item["IAP"],
                                                                                                                      item["Developer_badge"],
                                                                                                                      item["Physical_address"], 
                                                                                                                      item["Video_URL"],
                                                                                                                      item["Developer_ID"]))
                    
    # if commit:
        # self.conn.commit()
