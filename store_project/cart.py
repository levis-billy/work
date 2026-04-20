import sqlite3
connection = sqlite3.connect('store_transaction.db')
cursor = connection.cursor()
#cart Table

command6 = """CREATE TABLE IF NOT EXISTS cart (
   Cart_id INTEGER PRIMARY KEY,
    Customer_id TEXT,
    Product_id INTEGER,
    Quantity INTEGER,
FOREIGN KEY (Customer_id) REFERENCES customer(customer_id),
FOREIGN KEY (Product_id) REFERENCES products(product_id)
)"""
cursor.execute(command6)
cursor.execute("INSERT INTO cart VALUES (1, '2006', 1, 2)")
cursor.execute("INSERT INTO cart VALUES (2, '2011', 2, 1)")
cursor.execute("INSERT INTO cart VALUES (3, '2001', 3, 4)")
cursor.execute("SELECT * FROM cart")
results = cursor.fetchall()
connection.commit()