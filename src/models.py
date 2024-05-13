import datetime
from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# class User(Base):
#     __tablename__ = "users"
    
#     id = Column(Integer,primary_key=True)
#     user_name = Column(String)
#     email = Column(String, unique=True, index=True)
#     password = Column(String)
    

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer,primary_key=True)
    title = Column(String) 
    is_complete = Column(Boolean,default=False)
    created_at = Column(DateTime,default=datetime.datetime.now())
    # owner_id = Column(Integer,ForeignKey("User.id"))
