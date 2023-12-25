from sqlalchemy import create_engine # type = ignore
from sqlalchemy.ext.declarative import declarative_base # type = ignore
from sqlalchemy.orm import sessionmaker # type = ignore
from sqlalchemy.engine import Engine




SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:lalani@localhost/fastapi'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency
def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()