
from ..utils import *
from .. import database, models, oauth2, schemas
from sqlalchemy.orm import Session
from fastapi import FastAPI, status, HTTPException, Depends, APIRouter

route = APIRouter(
    prefix="/votes",
    tags=["VOTES"]
)


## creating a vote
@route.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote,  db: Session = Depends(database.get_db), user_id: int = Depends(oauth2.current_user)):

    # found_vote_check = db.query(models.Vote).filter(models.Vote.post_id==vote.post_id).first()
    # if not found_vote_check:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post doesn't exits")

    found_vote_query = db.query(models.Vote).filter(models.Vote.post_id==vote.post_id, models.Vote.user_id == user_id.id)
    found_vote = found_vote_query.first()

    if(vote.dir==1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"User {user_id.id} cannot like the same post again") 
        new_vote = models.Vote(user_id = user_id.id, post_id = vote.post_id)
        db.add(new_vote)
        db.commit()
        return {"message": "successfully added the vote"}

    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post doesn't exits")
        else:
            found_vote_query.delete(synchronize_session=False)
            db.commit()
            return {"message":"Post Deleted"}