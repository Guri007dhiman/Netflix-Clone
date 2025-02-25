import sqlite3

# Connect to the database (or create it if it doesn't exist)
connection = sqlite3.connect('netflixweb.db')

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        full_name TEXT NOT NULL,
        gmail TEXT NOT NULL,
        password TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        country TEXT NOT NULL
    )
''')

# Commit the changes and close the connection
connection.commit()
connection.close()

print("Table created successfully.")
