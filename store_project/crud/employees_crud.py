from database import get_connection
def get_all_employees():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    conn.close()

    return employees
#get employee by id 
def get_employee_by_id(employee_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees WHERE employee_id = ?", (employee_id,))
    employee = cursor.fetchone()
    conn.close()
    return employee

#add new employee
def add_employee(employee):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO employees
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            employee.employee_id,
            employee.first_name,
            employee.last_name,
            employee.position,
            employee.salary
        )
    )
    conn.commit()
    conn.close()
    return {"message": "Employee added successfully"}
