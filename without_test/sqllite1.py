import sqlite3
import random

# Create SQLite database
conn = sqlite3.connect("data_structures.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS data (
        key INTEGER PRIMARY KEY,
        value INTEGER
    );
''')
conn.commit()

# Create tables
def generate_fake_data(size):
    # Generate fake data using random values
    return {i: random.randint(1, 10000) for i in range(size)}

def insert_data_into_database(data):
    # Insert data into the 'data' table in the database
    for key, value in data.items():
        cursor.execute("INSERT OR REPLACE INTO data (key, value) VALUES (?, ?)", (key, value))
    conn.commit()
    
data_size = 100000
fake_data = generate_fake_data(data_size)

    # Insert fake data into the database
insert_data_into_database(fake_data)

# Commit changes and close connection
conn.commit()
conn.close()
