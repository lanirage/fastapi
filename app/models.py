from sqlalchemy import Column , INTEGER, String, Boolean , DateTime, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from . database import Base 

class Post(Base):
    __tablename__ ="post"
    id = Column(INTEGER, primary_key =True, nullable = False)
    title = Column(String, nullable = False)
    content = Column(String, nullable = False)
    published = Column(Boolean, server_default='TRUE', nullable=True)
    created_at =Column(TIMESTAMP(timezone=True), nullable=False, 
                       server_default = text('now()') )
    user_id = Column(INTEGER, ForeignKey("user.id" , ondelete= "Cascade"), nullable=False)

class User(Base):
    __tablename__ ="user"
    id = Column(INTEGER, primary_key =True, nullable = False)
    email = Column(String, unique= True, nullable = False)
    password = Column(String, nullable = False)
    created_at =Column(TIMESTAMP(timezone=True), nullable=False, 
                       server_default = text('now()') )
    
                  