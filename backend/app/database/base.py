from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.mixins import SoftDeleteMixin
from app.database.mixins import TimestampMixin
from app.database.mixins import UUIDMixin


class Base(DeclarativeBase):
    pass


class BaseModel(
    Base,
    TimestampMixin,
    UUIDMixin,
    SoftDeleteMixin,
):
    """
    Enterprise base model.

    Every GIIP model
    should inherit from this class.
    """

    __abstract__ = True

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )
