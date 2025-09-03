from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class OrganisationDB(Base):
    __tablename__ = "organisation"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    org_name = Column(String, index=True)

    roles = relationship("RoleDB", back_populates="organisation", cascade="all, delete-orphan")
    employees = relationship("EmployeeDB", back_populates="organisation_rel", cascade="all, delete-orphan")

class RoleDB(Base):
    __tablename__ = "role"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    role_name = Column(String, index=True)
    organisation_id = Column(Integer, ForeignKey("organisation.id"))

    organisation = relationship("OrganisationDB", back_populates="roles")
    employees = relationship("EmployeeDB", back_populates="role_rel", cascade="all, delete-orphan")

class EmployeeDB(Base):
    __tablename__ = "employees"  # plural!
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    title = Column(String)
    email = Column(String, unique=True, index=True)
    employee_number = Column(Integer, unique=True, index=True, nullable=False)

    organisation_id = Column(Integer, ForeignKey("organisation.id"))
    role_id = Column(Integer, ForeignKey("role.id"))

    organisation_rel = relationship("OrganisationDB", back_populates="employees")
    role_rel = relationship("RoleDB", back_populates="employees")