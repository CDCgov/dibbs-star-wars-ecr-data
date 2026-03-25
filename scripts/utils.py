import uuid
from datetime import datetime, timezone

def generate_uuid():
    return str(uuid.uuid4())


def generate_timestamp(value=None):
    """
    Generates a timestamp in YYYYMMDDHHMM-ZZZZ format.
    Defaults to current time if no value is provided.
    """
    # Use provided datetime object, or default to current UTC time
    dt = value if isinstance(value, datetime) else datetime.now(timezone.utc)

    # %Y: Year, %m: Month, %d: Day, %H: Hour, %M: Minute, %z: timezone offset (+HHMM or -HHMM)
    return dt.strftime("%Y%m%d%H%M%z")