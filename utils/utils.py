import datetime


def get_utc_now():
    """
    Simply returns datetime.datetime.utcnow(). This function makes testing easier, since datetime is a built-in type
    that can't be easily mocked.
    :return: datetime object with current UTC time
    """
    return datetime.datetime.utcnow()
