"""
# @Python program
# @Name: main.py
# @Lambda name: lambda_function_get_prescription_items
# @Since: December 2022
# @Author: Avinash
# @Version: 1.0
# @See: Program to get prescription item details from RDS
"""

from service.db_init import Connect
from models import PrescriptionsItems
from sqlalchemy import and_
from uuid import UUID
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import SQLAlchemyError
from common.exceptions import BadRequest

result = {}
conn = Connect()
Session = conn.connect()

def get_prescription_items(event,context):

    """
    Title:
        Handler function for this lambda function
    Args:
        event: Parameter to receive event data like JSON, DIC.
        context: Parameter for runtime information from LambdaContext type.
    Returns:
        Prescription item details as JSON.
    """

    try:
        session = Session()
        prescription_id = event["params"]["querystring"]["prescriptionId"].strip()
        drug_id = event["params"]["querystring"]["drugId"].strip()
        UUID(prescription_id)
        UUID(drug_id)
        all_data = session.query(PrescriptionsItems).where(and_(
                   (PrescriptionsItems.prescription_id == prescription_id),
                   (PrescriptionsItems.drug_id == drug_id)))
        prescription_item = all_data.one()
        result = prescription_item.get_prescriptions_items()
    except ValueError:
        raise BadRequest("Missing details")
    except NoResultFound:
        raise BadRequest("No data found")
    except SQLAlchemyError:
        raise BadRequest("SQLAlchemy Error")
    finally:
        session.close()

    return result