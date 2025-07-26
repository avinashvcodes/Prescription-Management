
class APIGatewayLambdaAuthorizer:

    def __init__(self, method_arn, authorizer, rbac_manager = None):
        self.method_arn = method_arn
        self.authorizer = authorizer
        self.rbac_manager = rbac_manager

    def authorize(self) -> bool:

        if not self.authorizer.authorize():
            return False

        if not self.rbac_manager:
            return True

        return self.rbac_manager.has_permission(self.authorizer.verified_payload, self.method_arn)
