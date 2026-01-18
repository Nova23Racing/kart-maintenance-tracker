CREATE TABLE karts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    chassis_model TEXT,
    engine_type TEXT,
    year INTEGER,
    status TEXT DEFAULT 'Active'
);

CREATE TABLE parts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kart_id INTEGER,
    part_name TEXT NOT NULL,
    installation_date DATE,
    lifespan_hours REAL,
    current_hours REAL DEFAULT 0,
    FOREIGN KEY (kart_id) REFERENCES karts (id)
);

CREATE TABLE maintenance_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kart_id INTEGER,
    part_id INTEGER,
    service_date DATE DEFAULT CURRENT_TIMESTAMP,
    description TEXT NOT NULL,
    technician_notes TEXT,
    FOREIGN KEY (kart_id) REFERENCES karts (id),
    FOREIGN KEY (part_id) REFERENCES parts (id)
);