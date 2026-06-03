from database import get_connection
#getting all cart items
def get_all_cart_items():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM cart")
    cart_items = cursor.fetchall() 
    conn.close()
    return cart_items   
#adding new cart items
def add_cart_item(cart_item):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO cart (product_id, quantity) VALUES (?, ?)", (cart_item.product_id, cart_item.quantity))
    conn.commit()
    conn.close()
    return cart_item
