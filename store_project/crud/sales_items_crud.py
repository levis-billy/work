from database import get_connection
#getting all sales items
def get_all_sales_items():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM salesitems")
    sales_items = cursor.fetchall() 
    conn.close()
    return sales_items
#get sales item by id
def sales_items_by_id(sale_item_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM salesitems WHERE sale_item_id = ?", (sale_item_id,))
    sales_item = cursor.fetchone()
    conn.close()
    return sales_item
#adding new sales item
def add_sales_item(sales_item):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO salesitems
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            sales_item.sales_id,
            sales_item.product_id,
            sales_item.quantity,
            sales_item.selling_price
        )
    )
    conn.commit()
    conn.close()
    return {"message": "Sales item added successfully"}
