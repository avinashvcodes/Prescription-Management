"""
# @Python program
# @Name: main.py
# @Lambda name: lambda_function_authorizer
# @Since: December 2022
# @Author: Avinash
# @Version: 1.0
# @See: Program to authenticate and authorize users
"""

from service.db_init import Connect
from sqlalchemy import and_
from models import Users
import re

db = Connect()
Session = db.connect()


def authorize(event, context):
    """
      Title:
          Handler function for this lambda function
      Args:
          event: Parameter to receive event data like JSON, DIC.
          context: Parameter for runtime information from LambdaContext type.
      Returns:
          Policy to authorize users.
      """

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email = event["headers"]["email"]
    password = event["headers"]["Password"]
    session = Session()

    if (re.fullmatch(regex, email)):
        all_user = session.query(Users).where(
            and_((Users.email == email), (Users.password == password))).all()
        if not all_user:
            effect = "Deny"
        elif all_user[0].is_admin:
            effect = "Allow"
        else:
            if "GET" in event["methodArn"]:
                effect = "Allow"
            else:
                effect = "Deny"
    else:
        effect = "Deny"

    return {
        "principalId": "yyyyyyyy",
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": effect,
                    "Resource": event["methodArn"]
                }
            ]
        },
        "context": {
            "a": "allowed"
        }
    }
