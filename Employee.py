from pydantic import BaseModel,EmailStr


class Employee(BaseModel):
    """
    A class to represent an employee within an organization.
    
    Attributes:
        first_name (str): The employee's first name.
        last_name (str): The employee's last name.
        email (EmailStr): The employee's email address.
        title (str): The employee's job title.
        role (str): The employee's role or position in the organization.
        employee_number (int/str): A unique employee identifier.
        organization (str): The name of the organization the employee works for.
    """

    first_name: str
    last_name: str
    email: EmailStr
    title: str
    role: str
    employee_number: int | str
    organisation: str
