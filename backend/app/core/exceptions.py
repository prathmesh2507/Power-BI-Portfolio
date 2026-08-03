class GIIPException(Exception):
    """Base exception for the project."""


class ValidationException(GIIPException):
    """Raised when validation fails."""


class DownloaderException(GIIPException):
    """Raised when download fails."""


class DatabaseException(GIIPException):
    """Raised when a database operation fails."""


class SchedulerException(GIIPException):
    """Raised when scheduler fails."""
