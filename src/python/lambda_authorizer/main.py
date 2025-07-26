import os

from .jwt_authorization import CognitoJWTAuthorizer
from .lambda_authorizer import APIGatewayLambdaAuthorizer
from .rbac_manager import RBACManager
from .utils import generate_policy

client_id = os.environ["CLIENT_ID"]
region = os.environ["REGION"]
domain = os.environ["DOMAIN"]
cognito_user_pool_id = os.environ["COGNITO_USER_POOL_ID"]

COGNITO_USER_POOL_URL = f"https://{domain}.{region}.amazonaws.com/{cognito_user_pool_id}"


def lambda_handler(event, context):
    """The Function used for authorization"""

    method_arn = event.get("methodArn")
    try:
        input_headers:dict[str,any] = event.get("headers", {})
        lower_case_headers = {key.lower(): value for key, value in input_headers.items()}
        jwt_token = lower_case_headers.get("authorization")

        if not jwt_token:
            return generate_policy("deny", method_arn)

        jwt_authorizer = CognitoJWTAuthorizer(jwt_token, COGNITO_USER_POOL_URL, client_id)
        rbac_manager = RBACManager()

        authorizer = APIGatewayLambdaAuthorizer(method_arn, jwt_authorizer, rbac_manager)

        if authorizer.authorize():
            return generate_policy("allow", method_arn)

        return generate_policy("deny", method_arn)

    except ValueError:
        return generate_policy("deny", method_arn)
