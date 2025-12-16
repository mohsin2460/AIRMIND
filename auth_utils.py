import os
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from passlib.context import CryptContext

pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET = os.getenv("JWT_SECRET")
ALG = "HS256"

def hash_password(p):
    return pwd.hash(p)

def verify_password(p, h):
    return pwd.verify(p, h)

def sign_token(sub):
    exp = datetime.now(timezone.utc) + timedelta(days=7)
    return jwt.encode({"sub": sub, "exp": exp}, SECRET, algorithm=ALG)

def verify_token(t):
    try:
        return jwt.decode(t, SECRET, algorithms=[ALG])
    except JWTError:
        raise ValueError("Bad token")
