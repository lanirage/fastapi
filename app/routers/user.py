from .. import models , Schemas, utils
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import database
from sqlalchemy.orm.session import Session

router = APIRouter(
   prefix= "/users",
   tags=['users']

)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Schemas.UserOut)
def create_user(user: Schemas.UserCreate, db: Session = Depends(database.get_db)):

      # hash the password - user.password
   hashed_password = utils.hash(user.password)
   user.password = hashed_password
   
   new_user= models.User(**user.dict())
   db.add(new_user)
   db.commit()
   db.refresh(new_user)
   return new_user 

@router.get('/{id}', response_model=Schemas.UserOut)
def get_user(id: int, db: Session = Depends(database.get_db), ):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} does not exist")

    return user
