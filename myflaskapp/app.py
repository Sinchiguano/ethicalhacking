from flask import Flask
from flask import render_template,request



app=Flask(__name__)

# @app.route('/')
# def home():
#     return 'Hello World'

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        # Here you can add code to save the user data to the database
        import sqlite3
        connection=sqlite3.connect('users.db')
        cursor=connection.cursor()
        cursor.execute('INSERT INTO users (name, password) VALUES (?, ?)', (name, password))
        connection.commit()
        connection.close()
        return 'User registered successfully!'
    return render_template('register.html')



if __name__ == '__main__':
    app.run(debug=True)