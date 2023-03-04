from datetime import datetime, timezone
from dateutil import parser as dateParser

def time_until(futureTime:str):
    """Get the about of time until futureTime

    Args:
        futureTime (str): time in ISO 8601 format (e.g. '2023-02-26T10:00:00.000Z')
    """
    return dateParser.parse(futureTime) - datetime.now(timezone.utc)