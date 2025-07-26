import base64
import json

import requests
from authlib.jose import JsonWebKey, jwt
from authlib.jose.errors import JoseError

from common.exceptions import PublicKeyNotFound

jwks_cache = {}

class CognitoJWTAuthorizer:
    """Handles JWT token verification and extraction"""

    def __init__(self, jwt_token, cognito_user_pool_url, client_id=None):
        self.jwt_token = jwt_token
        self.cognito_user_pool_url = cognito_user_pool_url
        self.client_id = client_id
        self._decoded_payload = None
        self._header = None
        self._verified_payload = None

    @property
    def verified_payload(self) -> dict:
        return self._verified_payload

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
        try:
            if self._header is None:
                header_b64 = self.jwt_token.split('.')[0]
                header_bytes = base64.urlsafe_b64decode(self.pad_base64(header_b64))
                self._header = json.loads(header_bytes)
            return self._header
        except (IndexError, json.JSONDecodeError) as e:
            raise ValueError(f"Invalid JWT header: {str(e)}") from e

    def get_unverified_payload(self) -> dict:
        try:
            if self._decoded_payload is None:
                payload_b64 = self.jwt_token.split('.')[1]
                payload_bytes = base64.urlsafe_b64decode(self.pad_base64(payload_b64))
                self._decoded_payload = json.loads(payload_bytes)
            return self._decoded_payload
        except (IndexError, json.JSONDecodeError) as e:
            raise ValueError(f"Invalid JWT payload: {str(e)}") from e 

    def validate(self):

        try:
            jwks = self.get_jwks()
            decoded_header = self.get_unverified_header()
            kid = decoded_header.get("kid")
            if not kid:
                return False
            rsa_key = self.get_public_key(jwks, kid)

            claims = jwt.decode(
                self.jwt_token,
                rsa_key,
                claims_options={
                    "iss": {
                        "essential": True,
                        "value": self.cognito_user_pool_url
                    },
                    "exp": {"essential": True}
                })
            claims.validate()
            self._verified_payload = dict(claims)
            return True
        except (JoseError, PublicKeyNotFound, ValueError):
            return False

    def authorize(self):
        if not self.validate():
            return False
        if self.client_id:
            return self._verified_payload.get("client_id") == self.client_id
        return True
