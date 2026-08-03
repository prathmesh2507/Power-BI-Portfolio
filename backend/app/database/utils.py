from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.core.logger import get_logger

logger = get_logger(__name__)


class DatabaseUtils:
    """
    Utility methods for common
    database operations.
    """

    @staticmethod
    def commit(db: Session):
        try:
            db.commit()

        except SQLAlchemyError as error:

            db.rollback()

            logger.exception(
                "Database commit failed."
            )

            raise error

    @staticmethod
    def rollback(db: Session):

        db.rollback()

    @staticmethod
    def execute_raw_sql(
        db: Session,
        query: str,
    ):

        return db.execute(text(query))
