
from flask import Flask
from flask import render_template, request

import sqlite3
app=Flask(__name__)

@app.route('/')
# def home():
#     return "Welcome to the Ethical Hacking Web Development Lab"

def home():
    return render_template('home.html')



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        
        connection=sqlite3.connect('user.db')
        cursor=connection.cursor()
        
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                       (username, password))
        connection.commit()
        connection.close()
        return "Registration successful"
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        
        connection=sqlite3.connect('user.db')
        cursor=connection.cursor()
        
        # cursor.execute("SELECT * FROM users WHERE username=? AND password=?",
        #                (username, password))
        
        cursor.execute("SELECT * FROM users WHERE username='{username}' AND password='{password}'")
        user = cursor.fetchone()
       
        
        
        user=cursor.fetchone()
        connection.close()
        
        if user:
            return "Login successful"
        else:
            return "Invalid credentials"
    return render_template('login.html')




if __name__=='__main__':
    app.run(debug=True)

