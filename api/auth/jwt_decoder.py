import os
from typing import Dict

import jwt

# Should be in os.env. This is not production ready code!
# Only for testing
JWT_SECRET = os.environ.get("jwt_token", "please_please_update_me_please")
JWT_ALGORITHM = os.environ.get("jwt_algorithm", "HS256")


class JWTDecoder:
    @staticmethod
    def encode(user_email: str) -> Dict[str, str]:
        payload = {"sub": user_email}
        return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    @staticmethod
    def decode(token: str) -> dict:
        try:
            return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        except jwt.exceptions.DecodeError:
            return {}
