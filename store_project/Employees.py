import sqlite3
connection = sqlite3.connect('store_transaction.db')
cursor = connection.cursor()
#customers table
command3 = """CREATE TABLE IF NOT EXISTS
employees (employee _id TEXT PRIMARY KEY,
first_name TEXT,
last_name TEXT,
role TEXT,
salary INTEGER,
hire_date TEXT
)"""
cursor.execute(command3)
cursor.execute("INSERT INTO employees VALUES ('800', 'Henry', 'Onyango', 'Cashier', 9000,'27 FEB 2026')")
cursor.execute("INSERT INTO employees VALUES ('900', 'Ruth', 'Ajwang', 'Manager', 30000, '24 Feb 2026')")
cursor.execute("SELECT * FROM employees")
results = cursor.fetchall()
connection.commit()
print(results)

