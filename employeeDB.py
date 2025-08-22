from sqlalchemy import Column, Integer, String
from database import Base


class EmployeeDB(Base):
    """
    Database model for the 'employees' table.

    Represents an employee in the system with personal, professional,
    and organizational details. This SQLAlchemy ORM model maps to the
     'employees' table in the database and includes constraints
    and indexes to ensure data integrity and query performance.

    Attributes:
        id (int): Primary key. Unique identifier for the employee record.
        first_name (str): Employee's first name. Indexed for faster search
         operations.
         last_name (str): Employee's last name. Indexed for faster search
         operations.
        title (str): Job title or designation of the employee
        (e.g., 'Software Engineer').
        organisation (str): Name of the organization the employee belongs to.
        employee_number (int): Unique number assigned to the employee. Must be
         unique across records and is indexed.
        role (str): Functional or security role within the system
        (e.g., 'Admin', 'User').
        email (str): Employee’s email address. Must be unique and is
        indexed for fast lookups.

    Table:
        employees: Stores employee records with unique constraints on email and
        employee_number.

    Indexes:
        - first_name
        - last_name
        - employee_number
        - email

    Unique Constraints:
        - email
        - employee_number

    Example:
        employee = EmployeeDB(
            first_name="John",
            last_name="Doe",
            title="Mr",
            organisation="Tech Corp",
            employee_number=1001,
            role="Engineer",
            email="john.doe@techcorp.com"
        )
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
