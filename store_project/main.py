from unicodedata import category

from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from crud.cart_crud import get_all_cart_items
from database import get_connection
from crud.products_crud import (get_all_products, get_product_by_id, add_product, get_products_by_category)
from crud.sales_items_crud import get_all_sales_items, sales_items_by_id, add_sales_item
from crud.employees_crud import get_all_employees, get_employee_by_id, add_employee
from crud.cart_crud import get_all_cart_items, add_cart_item
from customers_crud import get_all_customers, get_customer_by_id, add_customer
from schema import ProductCreate, SalesItemsCreate, EmployeeCreate,CartItemCreate, CustomerCreate
app = FastAPI()

@app.get("/scalar")
def scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="My API Docs"
    )
@app.get("/products")
def get_products(Category: str | None = None):
    if Category:
        return get_products_by_category(Category)
    return get_all_products()

@app.get("/products/{Product_id}")
def read_product(Product_id: int):
    return get_product_by_id(Product_id)
@app.post("/products")
def create_product(product: ProductCreate):
    return add_product(product)
@app.get("/sales-items")
def get_sales_items():
    return get_all_sales_items()
@app.get("/sales-items/{sale_item_id}")
def read_sales_item(sale_item_id: int):
    return sales_items_by_id(sale_item_id)
@app.post("/sales-items")
def create_sales_item(sales_item: SalesItemsCreate):
    return add_sales_item(sales_item)

@app.get("/employees")
def get_employees():
    return get_all_employees()
@app.get("/employees/{employee_id}")
def read_employee(employee_id: int):    
    return get_employee_by_id(employee_id)
@app.post("/employees")
def create_employee(employee: EmployeeCreate):
    return add_employee(employee) 
@app.get("/cart")
def get_cart_items():
    return get_all_cart_items()
@app.post("/cart")
def create_cart_item(cart_item: CartItemCreate):    
    return add_cart_item(cart_item)
@app.get("/customers")
def get_customers():
    return get_all_customers()
@app.get("/customers/{customer_id}")
def read_customer(customer_id: str):    
    return get_customer_by_id(customer_id)
@app.post("/customers")def create_customer(customer: CustomerCreate):
    return add_customer(customer)