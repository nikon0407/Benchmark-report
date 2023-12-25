import sqlite3

conn = sqlite3.connect("data_structures.db")  # Replace with your actual database file
cursor = conn.cursor()

# Execute a SELECT query
cursor.execute("SELECT * FROM data")  # Replace with your actual table name
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the connection
conn.close()
