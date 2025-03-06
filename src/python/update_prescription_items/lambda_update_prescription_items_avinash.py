"""
# @Python program
# @Name: main.py
# @Lambda name: lambda_function_update_prescription_items_avinash
# @Since: December 2022
# @Author: Avinash
# @Version: 1.0
# @See: Program to update prescription items details to RDS
"""

from service.db_init import Connect
from models import PrescriptionsItems 
from sqlalchemy import and_
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import SQLAlchemyError
from common.bad_request import BadRequest
from common.validation import validate_uuid

conn = Connect()
Session = conn.connect()

def update_prescription_items(event,context):

    """
    Title:
        Handler function for this lambda function
    Args:
        event: Parameter to receive event data like JSON, DIC.
        context: Parameter for runtime information from LambdaContext type.
    Returns:
        Success message.
    """

    drug_id = event["body"]["drugId"]
    prescription_id = event["body"]["prescriptionId"]
    quantity = event["body"]["quantity"]
    updated_by = event["body"]["updatedBy"]
    error_column = []

    if not validate_uuid(drug_id):
        error_column.append("drug_id")

    if not validate_uuid(prescription_id):
        error_column.append("prescription_id")

    if quantity <= 0:
        error_column.append("quantity")
    
    if not updated_by or len(updated_by) > 120:
        error_column.append("updated_by")
    
    if error_column:
        raise BadRequest("Missing / Wrong details in ["+", ".join(error_column)+"]")

    try:
        session = Session()
        prescription_id = event["body"]["prescriptionId"]
        drug_id = event["body"]["drugId"]
        result = session.query(PrescriptionsItems).where(
            and_(
            (PrescriptionsItems.prescription_id == prescription_id),
            (PrescriptionsItems.drug_id == drug_id)
            )
            ).update(PrescriptionsItems.update_prescriptions_items(event["body"]))
        session.commit()
        if not result:
            raise NoResultFound()
    except NoResultFound:
        raise BadRequest("No Result Found Error")
    except SQLAlchemyError:
        raise BadRequest("SQLAlchemy Error")
    finally:
        session.close()

    return {
        "message": "Prescription item updated successfully"
    }