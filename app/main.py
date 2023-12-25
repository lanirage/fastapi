import sys
from typing import Optional, TYPE_CHECKING, List
from . import models

from fastapi import FastAPI, Response, status, HTTPException, Depends
from pydantic import BaseModel
from fastapi.params import Body
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .routers import post, user, auth

from . database import engine, Base 

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


# while True:
#    try:
#       conn = psycopg2.connect(host='localhost' ,  dbname='fastapi' , user='postgres' , password='lalani', 
#                           cursor_factory =psycopg2.extras.RealDictCursor)
#       cursor = conn.cursor()
#       print("connection is success")
#       break  

#    except Exception as error:
#       print("connection is failed")
#       time.sleep(2)
      

