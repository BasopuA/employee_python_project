class Employee:
    """
    A class to represent an employee within an organization.

    Attributes:
        first_name (str): The employee's first name.
        last_name (str): The employee's last name.
        email (str): The employee's email address.
        title (str): The employee's job title.
        role (str): The employee's role or position in the organization.
        employee_number (int/str): A unique employee identifier.
        organization (str): The name of the organization the employee works for.
    """

    def __init__(
        self,
        first_name: str,
        last_name: str,
        email: str,
        title: str,
        role: str,
        employee_number: int | str,
        organisation: str,
    ) -> None:
        """
        Initializes an Employee instance with the provided attributes.

        Args:
            first_name (str): The employee's first name.
            last_name (str): The employee's last name.
            email (str): The employee's email address.
            title (str): The employee's job title.
            role (str): The employee's role or function.
            employee_number (int/str): A unique identifier for the employee.
            organisation (str): The name of the employee's organization.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.title = title
        self.role = role
        self.employee_number = employee_number
        self.organisation = organisation

    def get_employee_details(self) -> dict:
        """
            This function returns a python dictional of an employee information.
        Returns:
            dict: A formatted string with the employee's details.
        """

        details = {
            "title": self.title,
            "name": self.first_name,
            "surname": self.last_name,
            "email": self.email,
            "organisation_name": self.organisation,
            "employee_number": self.employee_number,
            "role": self.role,
        }

        return details
