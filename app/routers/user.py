from ..schemas import *
from ..utils import *
from .. import database, models
from sqlalchemy.orm import Session
from fastapi import FastAPI, status, HTTPException, Depends, APIRouter

route = APIRouter(
    prefix="/user",
    tags=["USER"]
)


####################################
###creating a new user

@route.post("/create_user", status_code = status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(body: UserStruct, db: Session = Depends(database.get_db)):

    hashed_password = hash(body.password)
    body.password = hashed_password
    new_user = models.User(**body.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


### for finding a specific id in database
@route.get("/{id}", response_model=UserResponse)
def get_user_from_id(id: int, db: Session = Depends(database.get_db)):

    user_one = db.query(models.User).filter(models.User.id==id).first()
    
    if user_one is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"{id} is not found in database" )
    else:
        desired_user = user_one
    return desired_user