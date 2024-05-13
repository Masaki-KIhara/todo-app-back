from sqlalchemy.orm import Session
from . import models,schemas

# def get_users(db:Session,skip:int=0,limit:int=100):
#     return db.query(models.User).offset(skip).limit(limit).all()

# def create_user(db:Session,):
#     return ""

# def update_user(db:Session,):
#     return ""

def get_tasks(db:Session,skip:int=0,limit:int=100):
    return db.query(models.Task).offset(skip).limit(limit).all()

def create_task(db:Session,item:schemas.CreateTask):
    db_task = models.Task(title=item.title,is_complete=item.is_complete)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# def update_task(db:Session,):
#     return ""