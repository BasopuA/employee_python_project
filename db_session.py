# db_session.py
from database import SessionLocal


class DBSession:
    """
    Dependency provider for database sessions.

    Usage:
        db: Session = Depends(DBSession())
    """

    def __init__(self):
        self.db = None

    def __call__(self):
        """
        Makes the class instance callable by FastAPI dependency injection.
        Opens a new session when called and ensures cleanup.
        """
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
