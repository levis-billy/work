import sqlite3
connection = sqlite3.connect('store_transaction.db')
cursor = connection.cursor()
#sales items
command5 = """CREATE TABLE IF NOT EXISTS
salesitems (sale_item_id TEXT PRIMARY KEY,
sales_id TEXT,
product_id INTEGER,
quantity INTEGER,
FOREIGN KEY (sales_id) REFERENCES sales(sales_id),
FOREIGN KEY (product_id) REFERENCES  products(product_id)
)"""
cursor.execute(command5)
cursor.execute("INSERT INTO salesitems VALUES('900', '900', 14, 400)")
connection.commit()
results = cursor.fetchall()



