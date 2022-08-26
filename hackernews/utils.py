import datetime


def convert_unix_to_datetime(unix_timestamp) -> datetime.datetime:
    """convert unix timestamp to human
    readable datetime

    Args:
        unix_timestamp: Unix epoch time

    Returns:
        datetime: A datetime object that is equivalent to
        the unix_timestamp
    """
    return datetime.datetime.fromtimestamp(unix_timestamp)
