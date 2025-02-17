import sqlite3


connection = sqlite3.connect('netflixweb.db')


cursor = connection.cursor()


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


connection.commit()
connection.close()

print("Table created successfully.")
