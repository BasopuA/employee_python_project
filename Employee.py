class Employee:
    """
    A class to represent an employee within an organization.

    Attributes:
        first_name (str): The employee's first name.
        last_name (str): The employee's last name.
        email (str): The employee's email address.
        title (str): The employee's job title.
        role (str): The employee's role or position in the organization.
        employee_number (int): A unique employee identifier.
        organization (str): The name of the organization the employee works for.
    """

    def __init__(
        self, first_name, last_name, email, title, role, employee_number, organisation
    ):
        """
        Initializes an Employee instance with the provided attributes.

        Args:
            first_name (str): The employee's first name.
            last_name (str): The employee's last name.
            email (str): The employee's email address.
            title (str): The employee's job title.
            role (str): The employee's role or function.
            employee_number (int): A unique identifier for the employee.
            organisation (str): The name of the employee's organization.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.title = title
        self.role = role
        self.employee_number = employee_number
        self.organisation = organisation

    def __str__(self):
        """
        Returns
            str: a string representation of the Employee object.

        Returns:
            dict: A formatted string with the employee's details.
        """
        return {
            "Title: ": self.title,
            "name: ": self.first_name,
            "Surname: ": self.last_name,
            "Email: ": self.email,
            "Organisation: ": self.organisation,
            "Employee ID": self.employee_number,
            "Role: ": self.role,
        }
