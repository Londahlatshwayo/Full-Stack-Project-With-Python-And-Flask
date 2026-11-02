import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath((__file__)))

#A function that connects to our database with the connect method
def create_post(name, content):
    connection =sql.connect(path.join(ROOT, "database.db"))

    #A variable that lets us traverse the database to look for the specific data using the cursor method
    cursor = connection.cursor()

    #A variable that lets us traverse the database to look for the specific data using the cursor method
    cursor.execute("Insert into posts (name, content) values(?, ?)", (name, content))
    connection.commit()
    connection.close()

#A function that pulls specific posts from the database and displays them to our browser
def get_posts():
    connection = sql.connect(path.join(ROOT, "database.db"))
    cursor = connection.cursor()
    cursor.execute("Select * from posts")
    posts = cursor.fetchall()

    return posts