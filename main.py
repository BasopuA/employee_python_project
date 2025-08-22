"""
FastAPI Application for Employee Management

A FastAPI-based web service that exposes an API endpoint to retrieve
employee details from a PostgreSQL database using SQLAlchemy (ORM) and
async database connections. The application integrates Pydantic models
for response validation and supports lifecycle events for database
connection management.

Features:
- FastAPI application with async lifespan events for database connectivity
- GET endpoint `/employee-details/` returning a list of employees
- Integration with SQLAlchemy ORM and asyncpg via `databases` library
- Response model validation using Pydantic
- CORS middleware enabled for cross-origin requests
- Uvicorn ASGI server for high-performance async execution

Endpoints:
    GET /employee-details/
        Description: Retrieves a list of all employees from the database.
        Response: List of employee objects conforming to the `Employee`
        Pydantic model. Status Codes:
            200: Successful response with employee data.
            500: Internal server error (e.g., database unreachable).

Dependencies:
    - fastapi: Web framework for building APIs with automatic
    OpenAPI documentation.
    - uvicorn: ASGI server to serve the application.
    - sqlalchemy: ORM for database interactions.
    - databases: Async database support for PostgreSQL.
    - pydantic: Data validation and settings management.

Modules Used:
    employee: Contains the Pydantic model `Employee` for response
    serialization.
    employeeDB: SQLAlchemy ORM model `EmployeeDB` representing the
    'employees' table.
    database: Configuration module containing engine, SessionLocal,
     and Database instance.

Startup Behavior:
    - Creates all tables if they don't exist (via `Base.metadata.create_all`)
    - Establishes async database connection on startup
    - Closes connection gracefully on shutdown

How to Run:
    $ python main.py

The app will be available at:
    - http://0.0.0.0:8000
    - Swagger UI: http://0.0.0.0:8000/docs
    - ReDoc: http://0.0.0.0:8000/redoc
"""

from typing import List
import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from employee import Employee
from database import database, SessionLocal, engine
from contextlib import asynccontextmanager
from employeeDB import EmployeeDB, Base

# Create database tables
Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Manage application lifecycle events.

    This async context manager handles setup and cleanup tasks:
        - Connects to the database when the app starts.
        - Disconnects gracefully when the app shuts down.

    Args:
        app (FastAPI): The FastAPI application instance.

    Yields:
        None: Control is passed to the application.
    """
    await database.connect()
    print("Database connected.")
    yield
    await database.disconnect()
    print("Database disconnected.")


def get_db():
    """
    Dependency to provide a database session.

    Yields a SQLAlchemy session (`SessionLocal`) for use in route functions.
    Ensures the session is properly closed after use.

    Yields:
        Session: Database session instance.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Initialize FastAPI app
app = FastAPI(
    title="Employee Management API",
    description="An API to manage and retrieve employee records.",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/employee-details/", response_model=List[Employee], tags=["Employees"])
async def employee_details(db: Session = Depends(get_db)):
    """
    Retrieve a list of all employees from the database.
    This endpoint queries the `employees` table and returns all records,
    serialized using the `Employee` Pydantic model.

    Args:
        db (Session): Database session dependency injected via `get_db`.

    Returns:
        List[Employee]: A list of employee objects.

    Raises:
        HTTPException: If there is an internal error during the query.
    """
    try:
        employees = db.query(EmployeeDB).all()
        return employees
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error retrieving employees: {str(e)}"
        )


# Run the server if this script is executed directly
if __name__ == "__main__":
    """
    Entry point for running the FastAPI application with Uvicorn.

    This block ensures the server only starts when the script is run directly,
    not when imported as a module.

    Server Configuration:
        Host: 0.0.0.0 (accessible externally)
        Port: 8000
        Reload: Disabled (enable in development by adding `reload=True`)
    """
    uvicorn.run(app, host="0.0.0.0", port=8000)
