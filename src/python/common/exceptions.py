class BadRequest(Exception):
    pass

class PublicKeyNotFound(Exception):
    """Raised when the JWT's 'kid' does not match any key in the JWKS."""
    def __init__(self, kid: str):
        super().__init__(f"No public key found for kid: {kid}")
