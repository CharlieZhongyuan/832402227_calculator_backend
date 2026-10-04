import sqlite3
from datetime import datetime
DB_PATH = "calculator.db"
def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS calculation_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            expression TEXT NOT NULL,
            result TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
def insert_record(expression, result):
    conn = get_connection()
    cursor = conn.cursor()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        "INSERT INTO calculation_history (expression, result, created_at) VALUES (?, ?, ?)",
        (expression, str(result), now)
    )
    conn.commit()
    record_id = cursor.lastrowid
    conn.close()
    return record_id
def get_all_records():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM calculation_history ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]
def delete_record(record_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM calculation_history WHERE id = ?", (record_id,))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()
    return deleted > 0