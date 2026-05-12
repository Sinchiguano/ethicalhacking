import sqlite3


connection=sqlite3.connect('user.db')

cursor=connection.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS users(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT NOT NULL,
                   password TEXT NOT NULL)"""
               )
connection.commit()
connection.close()

print("Database created successfully")
