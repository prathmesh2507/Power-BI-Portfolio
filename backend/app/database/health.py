from sqlalchemy import text

from app.database.engine import engine
from app.core.logger import get_logger

logger = get_logger(__name__)


def check_database_connection():

    try:

        with engine.connect() as connection:

            connection.execute(text("SELECT 1"))

        logger.info(
            "Database connection successful."
        )

        return True

    except Exception as error:

        logger.exception(error)

        return False


def get_database_version():

    with engine.connect() as connection:

        version = connection.execute(
            text("SELECT VERSION()")
        )

        return version.scalar()

def ping_database():

    with engine.connect():

        return True

def count_tables():

    with engine.connect() as connection:

        result = connection.execute(

            text("""

                SELECT COUNT(*)

                FROM information_schema.tables

                WHERE table_schema=DATABASE()

            """)

        )

        return result.scalar()


