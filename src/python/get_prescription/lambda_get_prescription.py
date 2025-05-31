"""
# @Python program
# @Name: main.py
# @Lambda name: lambda_function_get_prescription_avinash
# @Since: December 2022
# @Author: Avinash
# @Version: 1.0
# @See: Program to get prescription details from RDS
"""

from service.db_init import Connect
from models import Prescriptions
from uuid import UUID
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import SQLAlchemyError
from common.bad_request import BadRequest

conn = Connect()
Session = conn.connect()

def get_prescription(event,context):
    """
    Title:
        Handler function for this lambda function
    Args:
        event: Parameter to receive event data like JSON, DIC.
        context: Parameter for runtime information from LambdaContext type.
    Returns:
        Prescription details as JSON.
    """

    try:
        session = Session()
        prescription_id = event["params"]["querystring"]["prescriptionId"].strip()
        UUID(prescription_id)
        all_data = session.query(Prescriptions).where(Prescriptions.prescription_id == prescription_id)
        get_data = all_data.one()
        result = get_data.get_prescription()
    except ValueError:
        raise BadRequest("Missing details")
    except NoResultFound:
        raise BadRequest("No data found")
    except SQLAlchemyError:
        raise BadRequest("SQLAlchemy Error")
    finally:
        session.close()

    return result