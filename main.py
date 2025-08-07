"""
This module defines a simple FastAPI application with a single endpoint
that returns hardcoded employee details.

It demonstrates the use of the Employee class and the FastAPI web framework.
"""

import fastapi as api
import uvicorn

from employee import Employee
from fastapi.responses import HTMLResponse

# Initialize the FastAPI application
app = api.FastAPI()

@app.get('/abc',response_class=HTMLResponse)
async def abc():
    name = 'sambo'
    return f'<button>{5+6}</button>'


@app.get("/home")
async def employeeDetails():
    """
    GET /home endpoint

    Returns:
        dict: A dictionary containing employee information.

    Description:
        This endpoint creates a hardcoded instance of the Employee class
        and returns its string representation as a dictionary.
        Useful for testing or demonstration purposes.
    """
    emp = Employee(
        'Lungile',
        'Sambo',
        'sambolungile7@gmail.com',
        'Miss',
        'Software Engineer',
        '111',
        'SARAO'
    )

    return emp.__str__()


if __name__ == '__main__':
    uvicorn.run(app)
