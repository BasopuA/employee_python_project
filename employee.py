
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field, field_validator

class Employee(BaseModel):
    """
    Base Pydantic model for employee data.

    Defines the core set of fields required to create or represent an employee.
    Used for data validation during input (e.g., POST requests) and ensures
    structured, type-safe payloads.

    Attributes:
        first_name (str): The employee's first name.
        last_name (str): The employee's last name.
        email (EmailStr): Validated email address of the employee.
        title (str): Job title or position (e.g., 'Software Engineer').
        role (str): Functional or system role (e.g., 'Admin', 'Developer').
        employee_number (int): Unique numeric identifier assigned to the
        employee. organisation (str): Name of the organisation the employee
        belongs to.
    """


    first_name: str
    last_name: str
    email: EmailStr
    title: str
    role: str
    employee_number: int
    organisation: str

    @field_validator("employee_number")
    def validate_employee_number(cls, v):
        if v <= 0:
            raise ValueError("Employee number must be positive.")
        if not (1000 <= v <= 9999):
            raise ValueError("Employee number must be exactly 4 digits.")
        return v

    model_config = {"extra": "forbid"}