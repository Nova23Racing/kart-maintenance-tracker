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

@app.route('/kart/<int:kart_id>')
def kart_details(kart_id):
    conn = get_db_connection()
    kart = conn.execute('SELECT * FROM karts WHERE id = ?', (kart_id,)).fetchone()
    parts = conn.execute('SELECT * FROM parts WHERE kart_id = ?', (kart_id,)).fetchall()
    conn.close()
    return render_template('kart_details.html', kart=kart, parts=parts)

@app.route('/add_part/<int:kart_id>', methods=('POST',))
def add_part(kart_id):
    part_name = request.form['part_name']
    install_date = request.form['install_date']
    lifespan = request.form['lifespan']

    conn = get_db_connection()
    conn.execute('INSERT INTO parts (kart_id, part_name, installation_date, lifespan_hours) VALUES (?, ?, ?, ?)',
                 (kart_id, part_name, install_date, lifespan))
    conn.commit()
    conn.close()
    return redirect(url_for('kart_details', kart_id=kart_id))

@app.route('/part/<int:part_id>', methods=('GET', 'POST'))
def part_logs(part_id):
    conn = get_db_connection()
    
    if request.method == 'POST':
        description = request.form['description']
        notes = request.form['notes']
        conn.execute('INSERT INTO maintenance_logs (part_id, description, technician_notes) VALUES (?, ?, ?)',
                     (part_id, description, notes))
        conn.commit()

    part = conn.execute('SELECT * FROM parts WHERE id = ?', (part_id,)).fetchone()
    logs = conn.execute('SELECT * FROM maintenance_logs WHERE part_id = ? ORDER BY service_date DESC', (part_id,)).fetchall()
    conn.close()
    return render_template('part_logs.html', part=part, logs=logs)

if __name__ == '__main__':
    app.run(debug=True)

