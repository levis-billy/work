import sqlite3 

connection = sqlite3.connect('store_transaction.db') 
cursor = connection.cursor()
#products table
command1 = """CREATE TABLE IF NOT EXISTS
products (Product_id INTEGER PRIMARY KEY, Product_name TEXT, Category TEXT, Cost_price INTEGER, Stock_quantity INTEGER, Supplier_id TEXT)"""

cursor.execute(command1)

cursor.execute("INSERT INTO products VALUES (14, 'Sugar', 'Grocery', 100, 400, '001')")
cursor.execute("INSERT INTO products VALUES (15,'Milk','Grocery', 200, 300, '001')")
cursor.execute("INSERT INTO products VALUES (16, 'Bread', 'Bakery', 56, 90, '001')")
#get results 
cursor.execute("SELECT * FROM products")
results = cursor.fetchall()
connection.commit()
print(results)

