from sqlalchemy import Column, Integer, String
from database import Base


class EmployeeDB(Base):
    """
    Database model for the 'employees' table.
    Attributes:
        id (int): Primary key.
        first_name (str): Employee's first name.
         last_name (str): Employee's last name.
        title (str): Employee's title.
        organisation (str): Name of the organization the employee belongs to.
        role (str): Job title of the employee.
        email (str): Employee’s email address.

    Table:
        employees: Stores employee records with unique constraints on email and
        employee_number.
    """

    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    title = Column(String)
    organisation = Column(String)
    employee_number = Column(Integer, unique=True, index=True)
    role = Column(String)
    email = Column(String, unique=True, index=True)
