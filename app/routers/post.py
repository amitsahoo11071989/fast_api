from ..schemas import *
from ..utils import *
from .. import database, models, oauth2
from sqlalchemy.orm import Session
from fastapi import FastAPI, status, HTTPException, APIRouter, Depends
from typing import List, Optional
from sqlalchemy import func

route = APIRouter(
    prefix="/post",
    tags=["POST"]
)

## to get all the posts
##@route.get("/get_all_posts", response_model=List[PostResponse])

@route.get("/get_all_posts", response_model=List[PostOut])
def root(db: Session = Depends(database.get_db),  limit: int = 20, skip: int = 0, search: Optional[str] = ""):
    ##all_posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    results_query = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Post.id==models.Vote.post_id, isouter = True).group_by(models.Post.id)
    print(results_query)
    results = results_query.filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    return results

    ##return all_posts

## to create a new posts
@route.post("/create_post", status_code = status.HTTP_201_CREATED, response_model=PostResponse)
def create_post(body: PostStruct, db: Session = Depends(database.get_db), user_id: int = Depends(oauth2.current_user)):
    

    new_post = models.Post(user_id = user_id.id, **body.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


### for finding a specific id in database
@route.get("/{id}", response_model=PostOut)
def get_post_from_id(id: int, db: Session = Depends(database.get_db)):

    #post_one = db.query(models.Post).filter(models.Post.id==id).first()
    results_query = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Post.id==models.Vote.post_id, isouter = True).group_by(models.Post.id).filter(models.Post.id==id)
    
    print(results_query)
    post_one = results_query.first()
    
    if post_one is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"{id} is not found in database" )
    else:
        desired_post = post_one
    return desired_post

## for updating a specfied post
@route.put("/{id}", response_model=PostResponse)
def update_post(id: int, body: PostStruct, db: Session = Depends(database.get_db), user_id: int = Depends(oauth2.current_user)):

    post_one_query = db.query(models.Post).filter(models.Post.id==id)

    post_one = post_one_query.first()

    if post_one is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"{id} is not found in database" )
    else:
        if post_one.user_id != user_id.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not otherized to delete posts")
    post_one_query.update(body.dict(), synchronize_session=False)
    db.commit()

    return post_one_query.first()

## deleteing a specified post
@route.delete("/{id}")
def update_post(id: int, db: Session = Depends(database.get_db), user_id: int = Depends(oauth2.current_user)):

    post_one_query = db.query(models.Post).filter(models.Post.id==id)
    post_one = post_one_query.first()
    

    if post_one is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"{id} is not found in database" )
    else:
        if post_one.user_id != user_id.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not otherized to delete posts")
    post_one_query.delete(synchronize_session=False)
    db.commit()
    return {"message":"Post Deleted"}

