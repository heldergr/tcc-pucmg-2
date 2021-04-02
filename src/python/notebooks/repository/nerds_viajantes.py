import pandas as pd
import mysql.connector as sql

# Database config properties
db = 'tcc'
user = 'root'
paswd = 'root'
host = 'localhost'

PUBLISHED_POSTS_QUERY = """
        select ID, post_date, post_content, post_title, post_name, post_modified, comment_count from wp_eeurng_posts where post_status = 'publish'
        """

def get_connection():
    conn = sql.connect(db=db,user=user,host=host,password=paswd,use_unicode=True,
        charset='utf8', auth_plugin='caching_sha2_password')
    return conn

def execute_query(query):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(PUBLISHED_POSTS_QUERY)
    return cur.fetchall()

def read_published():
    published_posts = execute_query(PUBLISHED_POSTS_QUERY)
    return pd.DataFrame(published_posts, 
        columns=['id', 'date', 'content', 'title', 'name', 'modified', 'comment_count'])