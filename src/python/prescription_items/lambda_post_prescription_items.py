"""
# @Python program
# @Name: main.py
# @Lambda name: lambda_function_post_prescription_items
# @Since: December 2022
# @Author: Avinash
# @Version: 1.0
# @See: Program to post prescription items details to RDS
"""

from service.db_init import Connect
from models import PrescriptionsItems
from sqlalchemy.exc import SQLAlchemyError
from common.exceptions import BadRequest
from common.validation import validate_uuid

db = Connect()
Session = db.connect()

def post_prescription_items(event,context):

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
    created_by = event["body"]["createdBy"]
    error_column = []

    
    if not validate_uuid(drug_id):
        error_column.append("drug_id")

    if not validate_uuid(prescription_id):
            error_column.append("prescription_id")

    if quantity <= 0:
        error_column.append("quantity")
    
    if not created_by or len(created_by) > 120:
        error_column.append("created_by")
    
    if error_column:
        raise BadRequest("Missing / Wrong details in ["+", ".join(error_column)+"]")

    try:
        session = Session()
        session.begin()
        post_data = PrescriptionsItems()
        post_data.create_prescriptions_items(event["body"])
        session.add(post_data)
        session.commit()
    except SQLAlchemyError:
        raise BadRequest("SQLAlchemy Error")
    finally:
        session.close()

    return {
        "message": "Prescription item created successfully"
    }
