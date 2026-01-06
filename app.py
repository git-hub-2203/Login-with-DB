from flask import Flask, render_template, redirect, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('info.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (name TEXT, email TEXT, country TEXT)')
    db.commit()
    cursor.close()
    db.close()



init_db()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    country = request.form['country']

    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute('INSERT INTO users (name, email, country) VALUES (?, ?, ?)', (name, email, country))
    db.commit()
    cursor.close()
    db.close()

    return redirect('/')


@app.route('/adm')
def users():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM users')
    INFO = cursor.fetchall()
    cursor.close()
    db.close()

    return render_template('adm.html', info=INFO)


if __name__ == '__main__':
    app.run(debug=True)