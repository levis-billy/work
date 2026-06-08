import sqlite3
connection = sqlite3.connect('store_transaction.db')
cursor = connection.cursor()    
#users table 
command6 = """CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    hashed_password TEXT NOT NULL
)"""
cursor.execute(command6)
cursor.execute("INSERT INTO users VALUES(1, 'peter', 'peter@example.com', 'hashed_password_1')")
cursor.execute("INSERT INTO users VALUES(2, 'john', 'john@example.com', 'hashed_password_2')")
cursor.execute("SELECT * FROM users")
results = cursor.fetchall()
connection.commit() 