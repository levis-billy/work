from database import get_connection
#get all customers
def get_all_customers():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customer")
    customers = cursor.fetchall()

    conn.close()

    return customers
#get customer by id
def get_customer_by_id(customer_id: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customer WHERE Customer_id = ?", (customer_id,))
    customer = cursor.fetchone()
    conn.close()
    return customer
#add new customer
def add_customer(customer):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO customer
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            customer.Customer_id,
            customer.First_name,
            customer.Last_Name,
            customer.phone,
            customer.loyalty_points
        )
    )
    conn.commit()
    conn.close()
    return {"message": "Customer added successfully"}       
