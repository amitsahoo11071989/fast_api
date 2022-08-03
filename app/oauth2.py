from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from .config import setting

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = setting.token_secret_key
ALGORITHM = setting.token_algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = setting.token_access_expire_minutes

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm= ALGORITHM)

    return encoded_jwt

def verify_access_token(token: str, credentials_exceptions):
    

    try:
        payload = jwt.decode(token, SECRET_KEY, [ALGORITHM])
        id: str = payload.get("user_id")

        if id is None:
            raise credentials_exceptions

        token_data = schemas.Tokendata(id = id)
    except JWTError:
        raise credentials_exceptions

    return token_data

def current_user(token: str= Depends(oauth2_scheme)):
    credentials_exceptions = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
    detail="Could not validate credentials", headers= {"WWW-Authenticate":"Bearer"})

    return verify_access_token(token, credentials_exceptions)









