from uuid import UUID
from datetime import datetime

def validate_uuid(uuid):
    try:
        UUID(uuid)
    except ValueError:
        return False
    return True

def validate_date(date):
    try:
        return bool(datetime.strptime(date, "%d-%m-%Y"))
    except ValueError:
        return False
