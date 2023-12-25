from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm.session import Session
from .. import database, models, Schemas, utils, oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm


router =APIRouter(
   tags= ['Authentication']
)

@router.post('/login')
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):

      user= db.query(models.User).filter(models.User.email == user_credentials.username).first()
      if not user:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Invalid Credentials")
   
      # if not utils.verify(user_credentials.password, user.password):
      #    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")

      access_token = oauth2.create_access_token(data = {"user_id" :user.id})
    
     
   
#    Create a token
#    Return token
      return {"token" : access_token, "token type": "bearer"}