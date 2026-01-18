import sqlite3
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    karts = conn.execute('SELECT * FROM karts').fetchall()
    conn.close()
    return render_template('index.html', karts=karts)

@app.route('/add', methods=('POST',))
def add_kart():
    name = request.form['name']
    chassis = request.form['chassis']
    engine = request.form['engine']
    year = request.form['year']

    conn = get_db_connection()
    conn.execute('INSERT INTO karts (name, chassis_model, engine_type, year) VALUES (?, ?, ?, ?)',
                 (name, chassis, engine, year))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)