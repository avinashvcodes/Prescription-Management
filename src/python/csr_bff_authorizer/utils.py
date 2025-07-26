def generate_policy(effect, method_arn):
    auth_response = {}
    if effect and method_arn:
        policy_document = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "FirstStatement",
                    "Action": "execute-api:Invoke",
                    "Effect": effect,
                    "Resource": method_arn,
                }
            ],
        }
        auth_response["policyDocument"] = policy_document
    return auth_response
