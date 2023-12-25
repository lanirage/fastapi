
from .. import models, Schemas, utils, database
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
#from ..database import get_db
from sqlalchemy.orm.session import Session
from typing import Optional, TYPE_CHECKING, List

router = APIRouter(
   prefix="/posts",
   tags=['posts']
)

@router.get("/", response_model=list[Schemas.Post])
def get_posts(db: Session = Depends(database.get_db)):
    # cursor.execute("""SELECT * FROM post""")
    # posts = cursor.fetchall()
    posts=db.query(models.Post).all()
    print(posts)
    #print(post)
    return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model =Schemas.Post)
def create_post(post: Schemas.PostCreate, db: Session = Depends(database.get_db)):
   # cursor.execute("""INSERT INTO post (title, content) VALUES (%s, %s) RETURING * """ , (post.title,post.content) )
   # created_post=cursor.fetchone()

   new_post= models.Post(**post.dict())
   db.add(new_post)
   db.commit()
   db.refresh(new_post)
   return new_post 



@router.get("/{id}", response_model=Schemas.Post)
def get_postid(id:int, db: Session = Depends(database.get_db)):
   # cursor.execute("""SELECT * FROM post WHERE id = %s """,(str(id)))
   # post = cursor.fetchone()
   post = db.query(models.Post).filter(models.Post.id == id).first()
   print(post)
   if not post:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"post with id:{id} not found")
   return post




@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)  
def delete_post(id: int, db: Session = Depends(database.get_db)):
   # cursor.execute("""DELETE FROM post WHERE id = %s RETURNING * """,(str(id)))
   # deleted_post = cursor.fetchone()
   # conn.commit()
                  
   post = db.query(models.Post).filter(models.Post.id == id)
   if post.first() == None :
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"post with id:{id} not found")  
    
   post.delete(synchronize_session=False)
   db.commit()
   return Response(status_code=status.HTTP_204_NO_CONTENT) 


@router.put("/{id}", response_model = Schemas.Post )  
def update_post(id: int, updated_post: Schemas.PostCreate, db: Session = Depends(database.get_db)):
   # cursor.execute("""UPDATE post SET title= %s, content = %s WHERE id = %s RETURNING *""",
   #                (post.title, post.content, (str(id))) )
   # updated_post = cursor.fetchone()
   # conn.commit()
   post_query = db.query(models.Post).filter(models.Post.id ==id)
   post = post_query.first()
   
   if post == None :
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"post with id:{id} not found")  

   post_query.update(updated_post.dict() ,synchronize_session=False)
   db.commit() 
   return post_query.first()






     
   
  

    

