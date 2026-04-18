import os
import jwt
from datetime import datetime, timedelta, timezone

def generateToken(email: str, uuid: str) -> str:
    JWT_SECRET = os.getenv("JWT_SECRET")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
    JWT_EXPIRATION_TIME = os.getenv("JWT_EXPIRATION_TIME")
    # Generate a JWT token
    jwt_token = jwt.encode(
        {
            "sub": uuid,
            "email": email,
            "exp": datetime.now(timezone.utc) + timedelta(minutes=int(JWT_EXPIRATION_TIME))
        },
        JWT_SECRET,
        algorithm=JWT_ALGORITHM
    )
    return jwt_token

def generateRefreshToken(email: str, uuid: str) -> str:
    JWT_SECRET = os.getenv("JWT_SECRET")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
    JWT_REFRESH_EXPIRATION_TIME = os.getenv("JWT_REFRESH_EXPIRATION_TIME")
    # Generate a JWT token
    refresh_token = jwt.encode(
        {
            "sub": uuid,
            "email": email,
            "exp": datetime.now(timezone.utc) + timedelta(days=int(JWT_REFRESH_EXPIRATION_TIME))
        },
        JWT_SECRET,
        algorithm=JWT_ALGORITHM
    )
    return refresh_token
