
from fastapi import FastAPI, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import database, models, utils, oauth2
from ..schemas import *
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

route = APIRouter(
    tags=["Authentication"]
)

@route.post("/login", response_model=Token)
def login(input_creds: OAuth2PasswordRequestForm = Depends() , db: Session = Depends(database.get_db)):
    
    login_one = db.query(models.User).filter(models.User.email== input_creds.username).first()
    
    if not login_one:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    
    if not utils.verify_user_login(input_creds.password, login_one.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid poassword")

    access_token = oauth2.create_access_token(data={"user_id": login_one.id})

    return {"access_token": access_token, "token_type": "bearer"}

