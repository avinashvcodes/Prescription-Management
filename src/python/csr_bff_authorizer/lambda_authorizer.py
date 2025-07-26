class APIGatewayLambdaAuthorizer:

    def __init__(self, method_arn, authorizer):
        self.method_arn = method_arn
        self.authorizer = authorizer

    def authorize(self) -> bool:
        return self.authorizer.authorize()
