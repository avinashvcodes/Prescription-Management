"""
# @Python program
# @Name: main.py
# @Lambda name: lambda_function_update_prescription_avinash
# @Since: December 2022
# @Author: Avinash
# @Version: 1.0
# @See: Program to update prescription details to RDS
"""

from service.db_init import Connect
from models import Prescriptions
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm.exc import NoResultFound
from common.bad_request import BadRequest
from common.validation import validate_uuid, validate_date

conn = Connect()
Session = conn.connect()

def update_prescription(event,context):

    """
    Title:
        Handler function for this lambda function
    Args:
        event: Parameter to receive event data like JSON, DIC.
        context: Parameter for runtime information from LambdaContext type.
    Returns:
        Success message.
    """

    prescription_id = event["body"]["prescriptionId"]
    physicians_id = event["body"]["physiciansId"]
    customer_id = event["body"]["customerId"]
    status = event["body"]["status"] 
    payment_method_code = event["body"]["paymentMethod"]["code"] 
    date = event["body"]["date"]
    updated_by = event["body"]["updatedBy"]
    error_column = []

    if not validate_uuid(prescription_id):
        error_column.append("prescription_id")

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

    if not updated_by or len(updated_by) > 120:
        error_column.append("updated_by")
        
    if error_column:
        raise BadRequest("Missing / Wrong details in ["+", ".join(error_column)+"]")

    try:
        session = Session()
        success = session.query(Prescriptions).where(
            Prescriptions.prescription_id == prescription_id
        ).update(
            Prescriptions.update_prescription(event["body"])
            )
        session.commit()
        if not success:
            raise NoResultFound()
    except NoResultFound:
        raise BadRequest("No Result Found Error")
    except SQLAlchemyError:
        raise BadRequest("SQLAlchemy Error")
    finally:
        session.close()

    return {
        "message": "Prescription updated successfully"
    }