from datetime import datetime, timezone


def get_current_time() -> datetime:
    """
    Get the current time in UTC format.
    :return: Current time in UTC format.
    """
    time = datetime.now(timezone.utc)
    return time
