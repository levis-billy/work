from database import get_connection

def get_all_products():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    conn.close()

    return products

#get product by id
def get_product_by_id(Product_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products WHERE Product_id = ?", (Product_id,))
    product = cursor.fetchone()
    conn.close()
    return product
#adding new products
def add_product(product):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO products
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            product.product_id,
            product.product_name,
            product.category,
            product.cost_price,
            product.stock_quantity,
            product.supplier_id
        )
    )
    conn.commit()
    conn.close()
    return {"message": "Product added successfully"}
def get_products_by_category(Category):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM products WHERE Category = ?",
        (Category,)
    )

    products = cursor.fetchall()

    conn.close()

    return products
