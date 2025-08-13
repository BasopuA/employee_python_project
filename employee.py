"""
Module for defining the Employee data model using Pydantic.

This module contains the Pydantic BaseModel for an Employee, which includes
validation for fields such as email and enforces structured data for use in APIs
or internal systems.
"""

from pydantic import BaseModel, EmailStr


class Employee(BaseModel):
    """
    Represents an employee within an organization.

    Attributes:
        first_name (str): The employee's first name.
        last_name (str): The employee's last name.
        email (EmailStr): The employee's email address (automatically validated).
        title (str): The employee's job title or position.
        role (str): The employee's functional or security role.
        employee_number (int | str): A unique identifier for the employee.
        organisation (str): The name of the organization the employee belongs to.
    """

    first_name: str
    last_name: str
    email: EmailStr
    title: str
    role: str
    employee_number: int | str
    organisation: str
