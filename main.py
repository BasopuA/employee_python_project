"""
A FastAPI application that creates and returns details of an Employee object.

Features:
- FastAPI application instance creation
- GET endpoint (`/employee-details`) for returning employee details
- Example use of a Pydantic model (Employee)
- Application served with Uvicorn

Modules:
    fastapi: Framework for building APIs.
    uvicorn: ASGI server for running FastAPI apps.
    employee: Module containing the Employee class.
"""

import fastapi as api
import uvicorn
from employee import Employee

app = api.FastAPI()

@app.get("/employee-details")
async def employee_details():
    """
    GET /employee-details
    Returns a sample Employee object.

    This endpoint demonstrates creating an Employee instance with
    predefined attributes and returning it as JSON. If object creation
    fails, an error message is returned.

    Returns:
        Employee: The created Employee object in JSON format.
        dict: Error message if the Employee object could not be created.
    """
    try:
        employee: Employee = Employee(
            title="Miss",
            name="Lungile",
            surname="Sambo",
            email="sambolungile7@gmail.com",
            organisation_name="Software Engineer",
            employee_number=111,
            role="SARAO"
        )
        return employee
    except:
        return {"error": "Please verify the information you provided."}


if __name__ == '__main__':
    """
    Entry point for running the application.

    When this script is executed directly, it starts a Uvicorn ASGI server
    to run the FastAPI application. This block prevents the server from
    running when the module is imported elsewhere.
    """
    uvicorn.run(app)
