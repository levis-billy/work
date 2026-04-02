import sqlite3
connection = sqlite3.connect('store_transaction.db')
cursor = connection.cursor()
#sale table
command4 = """CREATE TABLE IF NOT EXISTS
sales (sales_id TEXT PRIMARY KEY,
sales_date TEXT,
employee_id TEXT,
Customer_id TEXT,
total_amount INTEGER,
payment_method TEXT,
FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
)"""
cursor.execute(command4)
cursor.execute("INSERT INTO sales VALUES('900', '30 JAN 2024','800', '2006', 2000, 'credit card')")
cursor.execute("INSERT INTO sales VALUES ('300', '14 FEB 2026', '400', '2011', 1200, 'Cash')")
cursor.execute("SELECT * FROM sales")
results = cursor.fetchall()
connection.commit()
print(results)

