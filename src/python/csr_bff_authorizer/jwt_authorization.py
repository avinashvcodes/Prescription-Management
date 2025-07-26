import base64
import json

import requests
from authlib.jose import JsonWebKey, jwt
from authlib.jose.errors import JoseError

from common.exceptions import PublicKeyNotFound

jwks_cache = {}

class CognitoJWTAuthorizer:

    def __init__(self, jwt_token, cognito_user_pool_url, client_id=None):
        self.jwt_token = jwt_token
        self.cognito_user_pool_url = cognito_user_pool_url
        self.client_id=client_id

    def get_jwks(self):
        if jwks_cache.get(self.cognito_user_pool_url):
            return jwks_cache[self.cognito_user_pool_url]
        jwks_url = f'{self.cognito_user_pool_url}/.well-known/jwks.json'
        response = requests.get(jwks_url, timeout=10)
        response.raise_for_status()
        jwks = response.json()
        jwks_cache[self.cognito_user_pool_url] = jwks
        return jwks

    def get_public_key(self, jwks_key, kid):
        for key in jwks_key["keys"]:
            if key["kid"] == kid:
                return JsonWebKey.import_key(key)
        raise PublicKeyNotFound(kid=kid)

    def pad_base64(self, s: str) -> str:
        return s + '=' * (-len(s) % 4)

    def get_unverified_header(self) -> dict:
        header_b64 = self.jwt_token.split('.')[0]
        header_bytes = base64.urlsafe_b64decode(self.pad_base64(header_b64))
        return json.loads(header_bytes)

    def get_unverified_payload(self) -> dict:
        payload_b64 = self.jwt_token.split('.')[1]
        payload_bytes = base64.urlsafe_b64decode(self.pad_base64(payload_b64))
        return json.loads(payload_bytes)

    def verify_jwt_token(self, kid) -> bool:
        try:
            jwks = self.get_jwks()
            rsa_key = self.get_public_key(jwks, kid)

            claims = jwt.decode(
                self.jwt_token,
                rsa_key,
                claims_options={
                    "iss": {
                        "essential": True,
                        "value": self.cognito_user_pool_url
                    }
                })
            claims.validate()
            return True
        except JoseError:
            return False
        except PublicKeyNotFound:
            return False

    def authorize(self) -> bool:
        decoded_payload = self.get_unverified_payload()
        unverified_client_id = decoded_payload.get("client_id")

        # verifies client_id if given
        if self.client_id and self.client_id != unverified_client_id:
            return False

        decoded_header = self.get_unverified_header()
        kid = decoded_header.get("kid")
        return self.verify_jwt_token(kid)
