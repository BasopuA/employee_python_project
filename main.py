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

@app.get("/employee-details/")
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
@app.post("/employee-create/")
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

###################################################################
if __name__ == "__main__":
    """
    Entry point for running the FastAPI application with Uvicorn.

    Starts the server only when executed directly (not on import).
    """
    uvicorn.run(app, host="0.0.0.0", port=8000)
