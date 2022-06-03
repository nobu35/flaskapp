import sqlite3

DATABASE = 'database.db'

def create_room_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS room (room_id,room_name)")
    con.close()

def create_tweet_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS tweet (room_id,tweet_id,tweet_text,user_name)")
    con.close()
