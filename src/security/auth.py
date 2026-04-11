from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from jose import jwt
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

load_dotenv()

secret_key = os.getenv("secret_key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 360

# Initialize the hasher
ph = PasswordHasher()

def hash_password(plain_password: str):
    """
    Hashes the password using Argon2id (default).
    No length limits, no manual salting required.
    """
    return ph.hash(plain_password)

def verify_password(plain_password: str, hashed_password: str):
    """
    Verifies the password. Returns True if match, False otherwise.
    """
    try:
        return ph.verify(hashed_password, plain_password)
    except VerifyMismatchError:
        return False
    except Exception:
        # Handles other potential errors like corrupted hashes
        return

# ------ Methods for user authentication and page traficc  -----

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=ALGORITHM)


    return encoded_jwt # Returning here the jwt token encoded




