"""
FastAPI application for managing employee records.

This service provides API endpoints to:
- Connect/disconnect from the PostgreSQL database on startup/shutdown.
- Retrieve all employee records.
- Create new employee records with validation and duplicate checks.

It uses SQLAlchemy for ORM, Pydantic for data validation, and Uvicorn as the ASGI server.
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from employee import Employee
from employee_db import EmployeeDB, Base
from database import database, engine, SessionLocal

# Create tables
Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(_app: FastAPI):
    """
    Handle application lifespan events.

    - On startup: connect to the database.
    - On shutdown: disconnect from the database.
    """
    await database.connect()
    print("Database connected.")
    yield
    await database.disconnect()
    print("Database disconnected.")


# Initialize FastAPI with lifespan
app = FastAPI(lifespan=lifespan)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://localhost:80",
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




def get_db():
    """
    Dependency that provides a database session.
    Ensures the session is closed after the request.
    """
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
############################################################

@app.get("/v1/employees/")
async def employee_details(db: Session = Depends(get_db)):
    """
    Retrieve all employee records from the database.

    Returns:
        List of employees or raises HTTP 500 if an error occurs.
    """
    try:
        employees = db.query(EmployeeDB).all()
        return employees
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error retrieving employees: {str(e)}",
        ) from e

###################################################################
@app.post("/v1/employees/")
async def employee_create(employee: Employee, db: Session = Depends(get_db)):
    """
    Create a new employee record in the database.

    Validates input using Pydantic and handles duplicate/invalid emails.

    Returns:
        Success message or raises HTTP 400 on integrity error.
    """
    db_employee = EmployeeDB(
        first_name=employee.first_name,
        last_name=employee.last_name,
        email=employee.email,
        title=employee.title,
        role=employee.role,
        employee_number=employee.employee_number,
        organisation=employee.organisation,
    )
    try:
        db.add(db_employee)
        db.commit()
        db.refresh(db_employee)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Employee already exists or your email is incorrect (example@email.com)",
        )

    return {"Message": "New employee has been created successfully."}

@app.put("/v1/employees/{id}")
async def employee_update(id: int, employee: Employee, db: Session = Depends(get_db)):
    """
    Update an existing employee record in the database.

    Args:
        id (int): The unique identifier of the employee to update.
        employee (Employee): The updated employee data (validated by Pydantic).
        db (Session): SQLAlchemy session dependency.

    Raises:
        HTTPException (404): If the employee with the given ID does not exist.

    Returns:
        dict: Success message confirming the employee was updated.
    """
    bd_employee = db.query(EmployeeDB).get(id)
    if bd_employee is None:
        raise HTTPException(detail="Employee not found", status_code=404)
    bd_employee.first_name = employee.first_name
    bd_employee.last_name = employee.last_name
    db.commit()
    return {"Message": "New employee has been updated successfully."}


@app.delete("/v1/employees/{id}")
async def employee_delete(id: int, db: Session = Depends(get_db)):
    """
    Delete an existing employee record from the database.

    Args:
        id (int): The unique identifier of the employee to delete.
        db (Session): SQLAlchemy session dependency.

    Raises:
        HTTPException (404): If the employee with the given ID does not exist.

    Returns:
        dict: Success message confirming the employee was deleted.
    """
    bd_employee = db.query(EmployeeDB).get(id)
    if bd_employee is None:
        raise HTTPException(detail="Employee not found", status_code=404)
    db.delete(bd_employee)
    db.commit()
    return {"Message": "Employee has been deleted successfully."}


@app.get("/v1/employees/{id}", response_model = Employee)
async def employee_details(id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single employee record by ID.

    Args:
        id (int): The unique identifier of the employee to fetch.
        db (Session): SQLAlchemy session dependency.

    Raises:
        HTTPException (404): If the employee with the given ID does not exist.

    Returns:
        EmployeeDB: The employee record from the database.
    """
    bd_employee = db.query(EmployeeDB).get(id)
    if bd_employee is None:
        raise HTTPException(detail="Employee not found", status_code=404)
    return bd_employee

if __name__ == "__main__":
    """
    Entry point for running the FastAPI application with Uvicorn.

    Starts the server only when executed directly (not on import).
    """
    uvicorn.run(app, host="0.0.0.0", port=8000)
