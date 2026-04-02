import sqlite3
connection = sqlite3.connect('store_transaction.db')
cursor = connection.cursor()
#customers Table
command2 = """CREATE TABLE IF NOT EXISTS customer
(Customer_id TEXT PRIMARY KEY,
First_name TEXT,
Last_Name TEXT,
phone TEXT,
loyalty_points INTEGER)"""
cursor.execute(command2)
cursor.execute("INSERT INTO customer VALUES ('2006', 'Levis', 'Omondi', '0711838134', 33)")
cursor.execute("INSERT INTO customer VALUES ('2011', 'Bravin', 'Otieno', '0715747286', 65)")
cursor.execute("INSERT INTO customer VALUES ('2001', 'Sally', 'Atieno','0790909090', 48)")
cursor.execute("SELECT * FROM customer")
results = cursor.fetchall()
connection.commit()
print(results)





