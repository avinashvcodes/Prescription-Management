
class RBACManager:

    def __init__(self):
        self.role_permissions = {
            "doctors": ["read", "write"],
            "staffs": ["write"]
        }

        self.method_permissions = {
            "GET": "read",
            "POST": "write",
            "PUT": "write",
            "PATCH": "write",
            "DELETE": "write"
        }

    def extract_roles_from_payload(self, jwt_payload):
        roles = []

        if 'cognito:groups' in jwt_payload:
            cognito_groups = jwt_payload['cognito:groups']
            if isinstance(cognito_groups, list):
                roles.extend(cognito_groups)
            elif isinstance(cognito_groups, str):
                roles.append(cognito_groups)

        return [role.lower() for role in roles if role]

    def extract_http_method_from_arn(self, method_arn):
        try:
            return method_arn.split("/")[2].upper()
        except (AttributeError, IndexError):
            return "GET"


    def has_permission(self, jwt_payload, method_arn):

        user_roles = self.extract_roles_from_payload(jwt_payload)
        if not user_roles:
            return False

        http_method = self.extract_http_method_from_arn(method_arn)

        required_permission = self.method_permissions.get(http_method)
        if not required_permission:
            return False

        for role in user_roles:
            role_permissions = self.role_permissions.get(role, [])
            if required_permission in role_permissions:
                return True

        return False
