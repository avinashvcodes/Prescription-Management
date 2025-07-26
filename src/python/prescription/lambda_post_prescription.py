"""
# @Python program
# @Name: main.py
# @Lambda name: lambda_function_post_prescription
# @Since: December 2022
# @Author: Avinash
# @Version: 1.0
# @See: Program to post prescription details to RDS
"""

from models import Prescriptions
from service.db_init import Connect
from sqlalchemy.exc import SQLAlchemyError
from common.exceptions import BadRequest
from common.validation import validate_uuid, validate_date

conn = Connect()
Session = conn.connect()

def post_prescription(event,context):

    """
    Title:
        Handler function for this lambda function
    Args:
        event: Parameter to receive event data like JSON, DIC.
        context: Parameter for runtime information from LambdaContext type.
    Returns:
        Success message.
    """

    physicians_id = event["body"]["physiciansId"]
    customer_id = event["body"]["customerId"]
    status = event["body"]["status"] 
    payment_method_code = event["body"]["paymentMethod"]["code"] 
    date = event["body"]["date"]
    created_by = event["body"]["createdBy"] 
    error_column = []

    if not validate_uuid(physicians_id):
        error_column.append("physicians_id")
    
    if not validate_uuid(customer_id):
        error_column.append("customer_id")

    if not status or len(status) > 1:
        error_column.append("status")
    
    if not payment_method_code or len(payment_method_code) > 3:
        error_column.append("payment_method_code")
    
    if not date or not validate_date(date):
        error_column.append("date")

    if not created_by or len(created_by) > 120:
        error_column.append("created_by")
        
    if error_column:
        raise BadRequest("Missing / Wrong details in ["+", ".join(error_column)+"]")

    try:
        session = Session()
        session.begin()
        post_data = Prescriptions()
        post_data.create_prescription(event["body"])
        session.add(post_data)
        session.commit()
    except SQLAlchemyError:
        raise BadRequest("SQLAlchemy Error")
    finally:
        session.close()

    return {
        "message": "Prescription created successfully"
    }
        
    
        
    
    