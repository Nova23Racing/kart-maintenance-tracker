import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO karts (name, chassis_model, engine_type, year) VALUES (?, ?, ?, ?)",
            ('N5R Alpha', 'Tony Kart 401RR', 'Vortex ROK GP', 2024)
            )

connection.commit()
connection.close()