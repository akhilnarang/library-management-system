from datetime import datetime

from zoneinfo import ZoneInfo


def current_time() -> datetime:
    """
    Returns the current time in UTC

    :return: A datetime object representing the current time in UTC
    """
    return datetime.now(tz=ZoneInfo("UTC"))
