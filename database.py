
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from databases import Database


# Load database URL from environment variable with fallback
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://anele:12345@localhost:5432/employee_management",
)
"""
str: The database connection string. Supports asyncpg for async operations.
     Falls back to a default PostgreSQL URL if not set in environment.
"""


# Synchronous engine for SQLAlchemy ORM (used with asyncpg in async context)
engine = create_engine(DATABASE_URL.replace("+asyncpg", ""))
"""
sqlalchemy.engine.Engine: Synchronous engine used for ORM operations.
Removes '+asyncpg' suffix to create a valid psycopg2/pg8000-compatible URL.
"""


# Session factory for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
"""
sqlalchemy.orm.sessionmaker: Factory for creating database sessions.
Configured for manual commit and flush to allow fine-grained transaction
 control.
"""


# Asynchronous database instance for async/await usage
database = Database(DATABASE_URL)
"""
databases.Database: Asynchronous database connection instance.
Used for async queries and operations in FastAPI or other async frameworks.
"""


# Base class for declarative models
Base = declarative_base()
"""
sqlalchemy.ext.declarative.api.DeclarativeMeta: Base class for all ORM models.
Models will inherit from this to link with the database metadata.
"""
