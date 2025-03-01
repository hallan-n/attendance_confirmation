from datetime import datetime, timedelta
from os import getenv
import bcrypt
from fastapi import HTTPException, Header
from jose import JWTError, jwt

def hashed(password: str):
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hash.decode("utf-8")


def check_hash(hashed: str, password: str):
    return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=int(getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
        )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, getenv("SECRET_KEY"), algorithm=getenv("ALGORITHM")
    )
    return encoded_jwt


def decode_token(token: str = Header(...)):
    try:
        payload = jwt.decode(
            token, getenv("SECRET_KEY"), algorithms=getenv("ALGORITHM")
        )
        return payload
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Token incorreto ou expirado.",
            headers={"WWW-Authenticate": "Bearer"},
        )
