from pyexpat import model
import typing
from fastapi import FastAPI##, status, HTTPException, Depends
from typing import List
import psycopg2
import time
from . import database, models
##from sqlalchemy.orm import Session
from .schemas import *
from .utils import *
from .routers import post,user,auth,votes
from .config import setting
from fastapi.middleware.cors import CORSMiddleware


##models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.route)
app.include_router(user.route)
app.include_router(auth.route)
app.include_router(votes.route)



@app.get("/")
def root():
    return {"message": "Hello World......"}

