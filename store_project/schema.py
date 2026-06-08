from pydantic import BaseModel

class ProductCreate(BaseModel):
    product_id: int
    product_name: str
    category: str
    cost_price: int
    stock_quantity: int
    supplier_id: str

class SalesItemsCreate(BaseModel):
    sales_id: int
    product_id: int
    quantity: int
    selling_price: int
class EmployeeCreate(BaseModel):
    employee_id: int
    first_name: str
    last_name: str
    position: str
    salary: int
class CartItemCreate(BaseModel):
    cart_id: int
    product_id: int
    quantity: int   

class CustomerCreate(BaseModel):
    customer_id: str
    first_name: str
    last_name: str
    phone: str
    loyalty_points: int