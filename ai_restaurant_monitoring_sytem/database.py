import sqlite3
from datetime import datetime

conn = sqlite3.connect('restaurant.db')
c = conn.cursor()

# Create tables
c.execute('''CREATE TABLE IF NOT EXISTS customers 
             (id INTEGER PRIMARY KEY, table_id INT, start_time DATETIME, end_time DATETIME)''')

c.execute('''CREATE TABLE IF NOT EXISTS staff_visits 
             (id INTEGER PRIMARY KEY, table_id INT, visit_time DATETIME)''')

def log_customer(table_id):
    c.execute("INSERT INTO customers (table_id, start_time) VALUES (?, ?)",
              (table_id, datetime.now()))
    conn.commit()

def log_staff_visit(table_id):
    c.execute("INSERT INTO staff_visits (table_id, visit_time) VALUES (?, ?)",
              (table_id, datetime.now()))
    conn.commit()